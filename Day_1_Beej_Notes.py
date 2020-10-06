'''
Graphs
-------
Nodes (also called "vertexes" or "verts" or "vertices") are connected by edges.

Edges *may* have numeric weights associated with them.
*If not shown, assume all weights are 1 ("unweighted graph")

Edges can be directed (one way) or undirected (two way)
* If there are only undirected edges, we call it an "undirected graph"
* Else we call it a "directed graph"

Cyclic: we can traverse and get back to the starting node somehow
* If a graph has any cycles in it, we call it a "cyclic graph"
* Else it is an "acyclic graph"

Representations of Graphs
-------------------------
Which nodes are adjacent ("directly connected") to a particular node.

Adjacency matrix:
* Big grid that has true/false values showing which nodes are adjacent
 * or edge weights

Adjacency list: will show a set for the nodes that the node connects to
A: goes to B, D {B, D}
B: goes to D, C {D, C}
C: goes to C, B {C, B}
D: goes to no one {}

'''
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Queue(): #FIFO Queue
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {} 
        #keys are all the verts in the graph, 
        #values are sets of adjacent verts 
    def add_vertex(self, vertex):
        #Add a new unconnected vert
        #Create the new key with the vertex ID, and set the value to an empty set (meaning no edges yet)
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v_from, v_to):
        #Add a directed edge to the graph
        #Fnd vertex v_from in our vertices, add v_to to the set of edges
        if v_from in self.vertices and v_to in self.vertices:
            self.vertices[v_from].add(v_to)
        else:
            raise IndexError("nonexistent vertex")

    def is_connected(self, v_from, v_to):
        if v_from in self.vertices and v_to in self.vertices:
            return v_to in self.vertices[v_from]
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, v):
        return self.vertices[v]

    def bft(self, starting_vertex_id):
        q = Queue()
        visited = set()
        #Init:
        q.enqueue(starting_vertex_id)
        #While the queue is not empty
        while q.size() > 0:
            v = q.dequeue()

            if v not in visited:
                print(v) #"Visit" the node
                
                visited.add(v)

                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)



g = Graph()
g.add_vertex(1)
g.add_vertex(2)
#now we have two nodes that are not connected (yet)
g.add_vertex(3)

#now, we want to connect them
g.add_edge(2, 1)
g.add_edge(1, 2) #now we will have an undirected graph because it goes both ways
g.add_edge(2, 3) #now 2 goes to 3 and 1, 3 goes to nothing

print(g.vertices)



'''
BFT

Init:
    Add the starting vert to the queue

While the queue is not empty:
    Pop current vert off queue
    If not visited:
        "visit" the node
        track it as visited
        add all its neighbors (adjacent)
'''

