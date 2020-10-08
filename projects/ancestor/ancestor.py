from collections import deque
#doubly ended queue great for quicker append and pop operations from both ends of container
from collections import defaultdict
#returns a dictionary-like object, never raises a keyError, provides default value for the key that doesn't exist
'''
Earliest Ancestor Problem

Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.


Clarifications:

The input will not be empty.
There are no cycles in the input.
There are no "repeated" ancestors – if two individuals are connected, it is by exactly one path.
IDs will always be positive integers.
A parent may have any number of children.

'''


#Will want to use DFS because we need graph to go as deep as we need to find the result, need to get to the end of the path
#Start from beginning to end, or end to beg, whichever is best to help

#Find earliest ancestor for some people in family tree

#INPUT: 
#  - LIST of relationships between parents and children spanning multiple generations in parent/child pairs
# - and INTEGER ID of individual in dataset we want to find earliest ancestor for

#OUTPUT:
# - returns an INTEGER
# - returns the earliest known ancestor, farthest from the input individual. 
# - if output is a tie, return lowest numeric ID
# - if output is None (no parents for the input child), return -1.

#ancestors = list of  pairs of parents, children
#starting_node = individual child, we want to find his ancestor

#Vertices = Person
#Edge = parent/child relationship
#Path = ancestor tree following generations of ancestors

#This graph will go from CHILD TO PARENT, until 



# class Stack():
#     def __init__(self):
#         self.stack = []
#     def push(self, value):
#         self.stack.append(value)
#     def pop(self):
#         if self.size() > 0:
#             return self.stack.pop()
#         else:
#             return None
#     def size(self):
#         return len(self.stack)

# def get_ancestors():
#     pass

def earliest_ancestor(ancestors, starting_node):
    graph = createGraph(ancestors)

    stack = deque()
    stack.append((starting_node, 0)) #starting_node, & distance from starting_node in a tuple
    visited = set() #so that we don't visit old nodes we've already visited
    earliestAncestor = (starting_node, 0) #keep track of earliestAncestor, that's what we will return
        #its a tuple with earliestAncestor's ID, and the distance! 
        #distance will compare if the relationship btw currNode and ancestor is earlier than the ancestor you've already found

    while len(stack) > 0:
        curr = stack.pop() #delete element from right end of stack. (current node, distance from starting node)
        currNode, distance = curr[0], curr[1] #assign to variables for easy reference
        visited.add(curr) #add to visited set

        if currNode not in graph: #if their key is not in the graph, then they have no more ancestors, its the furthest node you can get
            #if distance we found is greater than the distance we currently have (which is the spot index1 in the tuple (2nd)), then update it
            if distance > earliestAncestor[1]: 
                #update ancestor
                earliestAncestor = curr 
            elif distance == earliestAncestor[1] and currNode < earliestAncestor[0]:
                #update ancestor
                earliestAncestor = curr 
        else:
            #for ancestor in current node, if we haven't visited it yet, push it onto the stack
            for ancestor in graph[currNode]:
                if ancestor not in visited:
                    stack.append((ancestor, distance + 1)) #increment distance because its farther away
    # if the earliest ancestor is not ourself return it, if it is ourself (the starting node), then return -1
    return earliestAncestor[0] if earliestAncestor[0] != starting_node else -1

def createGraph(ancestors):
    #defaultdict allows you to set a default value
    #every key added to this dictionay will have a default value of an empty set
    graph = defaultdict(set)

    for edge in ancestors: #think of ancestors as edges, the relationships between child and parent
        #construct directed graph from child to parent
        #ancestor will be first in array,
        #child will be second in array
        ancestor, child = edge[0], edge[1]
        #add that to our graph, directed edge from child to ancestor
        graph[child].add(ancestor)

    return graph

# ancestorsForTesting = []
print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 6)) #prints 10
print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 7)) #prints 4
print(earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 9)) #prints 4, because it was a tie but printed lower numeric value