from queue import PriorityQueue
from collections import deque
import random
import tkinter as tk
import colorsys

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
            graph[path[i]].append((random.randint(-10, 10), path[i+1]))
        
        self.__graph = graph

    def bfs(self, start, end):
        # there is no need to traverse, the `start` is the `end`
        if start == end:
            return []
    
        # `paths` is the list of individual routes the algorithm explores
        paths = [[start]]
        path_num = 0
        visited = {start}
            
        while path_num < len(paths):
            current_path = paths[path_num] 
            current_node = current_path[-1] 
            neighbours = self.__graph[current_node]
            # make a list of `nodes` i.e. just the nodes/indexes into the graph
            # without weights.
            nodes = [node for weight, node in neighbours]
    
            # the target node, `end`, is among the neighbouring nodes, so the 
            # search can end here
            if end in nodes:
                path = current_path+[end]
                return path 
    
            for node in nodes:
                # iterate over each univisited node
                if not node in visited:
                    # the `current_path` is extended by the new `node` and added
                    # to paths
                    paths.append(current_path+[node]) 
                    visited.add(node) # the node is marked as visited
    
            # increment `path_num` to extend the next path
            path_num += 1
    
        # no path exists between the two nodes
        return []

# grid size
rows = 32
cols = 32
button_dim = 32

# list of references to the buttons
buttons = []

start = (0,0)
end = (rows-1, cols-1)
root = tk.Tk()

# def clear_path():
#     for child in root.children.values():
#         _, _, _, _, bg = child.configure()['background']
#         if bg == "red":
#             child.configure(bg="#888888")

START_COLOUR = "#FFD3D6"
END_COLOUR = "#F765A3"

def set_start(row, col, button):
    global start
    # change old #882288 to #888888
    old_row, old_col = start
    
    # change button just clicked to #882288
    button.configure(bg=START_COLOUR)
    start = row, col
#    clear_path()

def set_end(row, col, button):
    global end
    # change old #882222 to #888888
    old_row, old_col = end
    
    # change button just clicked to #882222
    button.configure(bg=END_COLOUR)
    end = row, col
#    clear_path()

# setup the grid of buttons
for row in range(rows):
    row_buttons = []
    for col in range(cols):
        button = tk.Frame(root, bg="#888888")
        button.place(x=col*button_dim, y=row*button_dim, width=button_dim, height=button_dim)
        button.bind("<Button-1>", lambda event, r=row, c=col, b=button: set_start(r, c, b))
        button.bind("<Button-3>", lambda event, r=row, c=col, b=button: set_end(r, c, b))
        row_buttons.append(button)
    buttons.append(row_buttons)

# load the graph
graph = Graph()
graph.load_maze(rows, cols)

# add the walls
for (x, y), neighbours in graph.as_dict().items():
    existing = [neighbour for weight, neighbour in neighbours]
    if (x,y-1) not in existing:
        wall = tk.Frame(root, bg="white")
        wall.place(x=x*button_dim, y=y*button_dim, width=button_dim, height=4)
    if (x,y+1) not in existing:
        wall = tk.Frame(root, bg="white")
        wall.place(x=x*button_dim, y=(y+1)*button_dim, width=button_dim, height=4)
    if (x-1,y) not in existing:
        wall = tk.Frame(root, bg="white")
        wall.place(x=x*button_dim, y=y*button_dim, width=4, height=button_dim)
    if (x+1,y) not in existing:
        wall = tk.Frame(root, bg="white")
        wall.place(x=(x+1)*button_dim, y=y*button_dim, width=4, height=button_dim)

# colour routes
def colour_routes():
    # Initialize the queue with the starting node
    queue = deque([(0, start)])
    # Set to keep track of visited nodes
    visited = set([start])
    
    while queue:
        # Dequeue a node from the front of the queue
        _, (x,y) = queue.popleft()
        h, s, v = hex_to_hsv(buttons[x][y].cget('bg'))
        
        # Enqueue all unvisited neighbours
        for weight, (i,j) in graph[(x,y)]:
            if (i,j) not in visited:
                buttons[i][j].configure(bg=hsv_to_hex((h-weight)%360, s, v))
                visited.add((i,j))
                queue.append((weight, (i,j)))

buttons[0][0].configure(bg=START_COLOUR)
buttons[rows-1][cols-1].configure(bg=END_COLOUR)

old_start = start
old_end = end
colour_routes()
root.update()

# tk loop
while True:
    # flip the path diagonally due to difference in coordinates
    if start != old_start:
        colour_routes()

    if start != old_start or end != old_end:
        (x, y), (i, j) = start, end
        path = graph.djikstras((y,x), (j,i))
        try:
            path.pop()
            path.pop(0)
            for y, x in path:
                #buttons[x][y].configure(bg="#000000")
                pass
        except:
            pass

    old_start = start
    old_end = end
    root.update_idletasks()
    root.update()
