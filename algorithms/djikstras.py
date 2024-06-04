from queue import PriorityQueue
from collections import deque
import random
import tkinter as tk
import colorsys
from gradpyent.gradient import Gradient

WHITE = "#FFFFFF"
MAX_WEIGHT = 10
start_colour = "#ffffff"
end_colour   = "#000000"

darks  = Gradient(gradient_start="#000000", gradient_end=start_colour).get_gradient_series(
        series=[i/1000 for i in range(1000)], fmt='html')
lights = Gradient(gradient_start=start_colour, gradient_end="#FFFFFF").get_gradient_series(
        series=[i/1000 for i in range(1000)], fmt='html')

grad_size = 100
grad = darks+Gradient(gradient_start=start_colour, gradient_end=end_colour).get_gradient_series(
       series=[i/grad_size for i in range(grad_size)], fmt='html')+lights

START_COLOUR = grad[len(grad)//2]

class Infinity:
    def __gt__(self, _): return True
    def __lt__(self, _): return False
    def __repr__(self): return "∞"

class Graph:
    def __getitem__(self, idx):
        return self.__graph[idx]

    def load_dict(self, d):
        """ Set the graph using a dictionary representation. """
        self.__graph = d
    
    def load_random(self, size, weight_range, avg_neighbour_count):
        """ Generate a graph of integer nodes randomly. """
        # Populate the graph with each node
        graph = {i: [] for i in range(size)}

        for _ in range(size * avg_neighbour_count):
            # Randomly generate two distinct numbers
            node1, node2 = random.sample(range(size), 2)
            if node1 not in graph[node2]:
                # Pick a random weight within the range
                weight = random.randint(1, weight_range)
                
                # Connect the nodes with a link of the same weight
                graph[node1].append((weight, node2))
                graph[node2].append((weight, node1))
        
        self.__graph = graph
    
    def as_dict(self): 
        """ Return the dictionary used to store the graph. """
        return self.__graph

    def djikstras(self, start, end):
        """ 
        Djikstra's Shortest Path Algorithm: finds shortest path between 
        two nodes.
        """
        current = start
        # Keep a running total of the weight of the full path traversed.
        # This starts at 0 as no distanced has been traverse.
        total = 0
        q = PriorityQueue()
        # routes = { node: (shortest_distance, node_to_it), ... }
        # Shortest distance is initialised to Infinity.
        # `node_to_it` is kept to trace back through the path followed. 
        routes = {node: (Infinity(), ' ') for node in self.__graph}

        while current != end:
            paths = self.__graph[current]
            for weight, node in paths:
                if node in routes:
                    if routes[node][0] > total+weight:
                        # If the weight to get there is greater than the 
                        # new weight update the weight set the node into 
                        # it to be current
                        routes[node] = total+weight, current
                        # Append this new route to the queue
                        q.put((total+weight, node))

            # If the queue is ever empty then a path does not exist
            if q.empty():
                return []
                
            # Total and current node becomes the first item in the 
            # priority queue (lowest weight)
            total, current = q.get()
        
        path = []
        while current != start:
            # Follow the routes backwards to find the shortest path
            path.append(current)
            _, current = routes[current]
        
        # Append the start node and reverse the list
        return (path+[start])[::-1]

    def load_maze(self, width, height):
        # create a blank grid
        grid = {}
        for x in range(width):
            for y in range(height):
                nodes = [(0, (i,j)) for i,j in [(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
                              if 0 <= i < width and 0 <= j < height ]
                grid[(x, y)] = nodes

        # traverse every node
        current = next(iter(grid))
        visited = {key: False for key in grid}
        stack = [current]
        visited[current] = True
        path = []
        while len(stack) > 0:
            path.append(current)
            unvisited = [n for _, n in grid[current] if not visited[n]]
            if len(unvisited) == 0:
                current = stack.pop()
            else:
                stack.append(current)
                current = random.choice(unvisited)
                visited[current] = True

        graph = {key: [] for key in grid}
        for i in range(len(path)-1):
            graph[path[i]].append((random.randint(0, MAX_WEIGHT), path[i+1]))
        
        self.__graph = graph

def hsv_to_hex(h, s, v):
    # Convert HSV (h: 0-360, s: 0-1, v: 0-1) to a hexadecimal color string.
    h = h / 360.0  # Convert hue to [0, 1]
    r, g, b = colorsys.hsv_to_rgb(h, s, v)
    return f'#{int(r*255):02x}{int(g*255):02x}{int(b*255):02x}'

def hex_to_hsv(hex_color):
    # Convert a hexadecimal color string to HSV (h: 0-360, s: 0-1, v: 0-1).
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    return h * 360, s, v  # Convert hue to [0, 360]

def set_start(row, col, button):
    global start
    old_row, old_col = start
    
    button.configure(bg=START_COLOUR)
    start = row, col
    x, y = start
    colour_routes((y,x))
    buttons[x][y].configure(bg=WHITE)
    draw_shortest_path()

def set_end(row, col, button):
    global end
    old_row, old_col = end
    
    end = row, col
    draw_shortest_path()

def colour_routes(start): # breadth-first
    global prev_end_colour
    # Initialize the queue with the starting node
    queue = deque([(0, start)])
    # Set to keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        _, (x,y) = queue.popleft()
        colour = buttons[y][x].cget('bg')
        
        # Enqueue all unvisited neighbours
        for weight, (i,j) in graph[(x,y)]:
            if (i,j) not in visited:
                idx = grad.index(colour) - (weight-MAX_WEIGHT//2)
                colour = grad[idx]
                buttons[j][i].configure(bg=colour)

                if (i,j) == end:
                    prev_end_colour = buttons[j][i].cget('bg')

                visited.add((i,j))
                queue.append((weight, (i,j)))

def draw_shortest_path():
    global prev_end_colour
    global old_end

    (x, y), (i, j) = start, end
    path = graph.djikstras((y,x), (j,i))
    for x in range(rows):
        for y in range(cols):
            for widget in buttons[x][y].winfo_children():
                if isinstance(widget, tk.Canvas):
                    widget.destroy()
    try:
        path.pop()
        path.pop(0)
        k, l = old_end
        buttons[k][l].configure(bg=prev_end_colour)
        prev_end_colour = buttons[i][j].cget('bg')
        buttons[i][j].configure(bg=WHITE)
        old_end = end
        for x, y in path:
            canvas = tk.Canvas(buttons[y][x], bg=buttons[y][x].cget('bg'), 
                               width=button_dim, height=button_dim, 
                               highlightthickness=0)
            canvas.create_oval(8, 8, button_dim-4, button_dim-4, fill=WHITE, 
                               outline=WHITE)
            canvas.bind("<Button-1>",lambda event,r=y,c=x,b=button:set_start(r,c,b))
            canvas.bind("<Button-3>",lambda event,r=y,c=x,b=button:set_end(r,c,b))
            canvas.pack()

    except Exception as e:
        print(e)

# grid size
rows = 60
cols = 60
button_dim = 12

start = (0,0) # corners
end = (rows-1, cols-1)
old_end = end

# start the window
root = tk.Tk()
root.configure(background=WHITE)

# load the graph
graph = Graph()
graph.load_maze(rows, cols)

# initialise the grid of buttons
buttons = [] # list of references to the buttons
for row in range(rows):
    row_buttons = []
    for col in range(cols):
        button = tk.Frame(root, bg=WHITE)
        button.place(x=col*button_dim, y=row*button_dim, width=button_dim, height=button_dim)
        button.bind("<Button-1>", lambda event, r=row, c=col, b=button: set_start(r, c, b))
        button.bind("<Button-3>", lambda event, r=row, c=col, b=button: set_end(r, c, b))
        row_buttons.append(button)
    buttons.append(row_buttons)

# add the walls
for (x, y), neighbours in graph.as_dict().items():
    existing = [neighbour for weight, neighbour in neighbours]
    if (x,y-1) not in existing:
        wall = tk.Frame(root, bg=WHITE)
        wall.place(x=x*button_dim, y=y*button_dim, width=button_dim, height=4)

    if (x,y+1) not in existing:
        wall = tk.Frame(root, bg=WHITE)
        wall.place(x=x*button_dim, y=(y+1)*button_dim, width=button_dim, height=4)

    if (x-1,y) not in existing:
        wall = tk.Frame(root, bg=WHITE)
        wall.place(x=x*button_dim, y=y*button_dim, width=4, height=button_dim+4)

    if (x+1,y) not in existing:
        wall = tk.Frame(root, bg=WHITE)
        wall.place(x=(x+1)*button_dim, y=y*button_dim, width=4, height=button_dim+4)

buttons[0][0].configure(bg=START_COLOUR)
colour_routes(start)

buttons[0][0].configure(bg=WHITE)
prev_end_colour = buttons[rows-1][cols-1].cget('bg')
buttons[rows-1][cols-1].configure(bg=WHITE)

# main tkinter input loop
root.mainloop()
