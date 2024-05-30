from queue import PriorityQueue
import random
import networkx as nx
import matplotlib.pyplot as plt

class Infinity:
    def __gt__(self, _): return True
    def __lt__(self, _): return False
    def __repr__(self): return "∞"

class Graph:
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

    def show_networkx(self):
        g = nx.Graph()

        for node, nodes in self.__graph.items():
            for weight, neighbour in nodes:
                g.add_edge(node, neighbour, weight=weight)
                
        node_colours, edge_colours = [], []
        for node in g:
            if node in path:
                node_colours.append('purple')
            else: 
                node_colours.append('pink')
                
        for node1, node2 in g.edges():
            if node1 in path and node2 in path:
                edge_colours.append('purple')
            else: 
                edge_colours.append('pink')
                
        pos = nx.spring_layout(g, k=1, iterations=200)
        nx.draw(g, pos, node_color=node_colours, edge_color=edge_colours, with_labels=True)
        edge_labels = nx.get_edge_attributes(g, "weight")
        nx.draw_networkx_edge_labels(g, pos, edge_labels)
        plt.show()

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
            graph[path[i]].append((random.randint(0, 20), path[i+1]))
        
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

graph = Graph()
"""
graph.load_dict({
    'A': [(4, 'B'), (9, 'C'), (5, 'D')],
    'B': [(4, 'A'), (14, 'F')],
    'C': [(9, 'A'), (7, 'D'), (4, 'E')],
    'D': [(5, 'A'), (7, 'C'), (3, 'H')],
    'E': [(4, 'C'), (6, 'G'), (4, 'H')],
    'F': [(14, 'B')],
    'G': [(6, 'E')],
    'H': [(3, 'D'), (4, 'E'), (8, 'I')],
    'I': [(8, 'H')], 
})
"""
graph.load_maze(3, 3)

print(graph.as_dict())

