'''
Connected Components

Part of the same graph, but the edges are not connected to some of the nodes. 
It looks like they might be a different graph, but we are imaging the nodes exist in the same data structure.
Clusters of nodes that are connected by edges = connected components. 

Separate "islands" in a graph
Example:
Graph nodes: A B C D E F
Graph edges: A,B  C,D  C,E  D,E



'''

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

row 5, col 4:
    neighbors:
        row 4, col 4
        row 6, col 4
        row 5, col 3
        row 5, col 5


