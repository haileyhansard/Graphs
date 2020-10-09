# from util import Queue

'''
Word Ladder Problem:

Given two words (begin_word and end_word), and a dictionary's word list,
return the shortest transformation sequence from begin_word to end_word, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin)word and end_word are non-empty and are not the same.

Sample: 
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
return: ['sail', 'bail', 'boil', 'bolt', 'boat']

begin_word = "hungry"
end_word = "happy"
return None

'''
#How can we phrase this problem using graph terms?
#What are the vertices and edges?
    #path = transformation sequence
    #shortest path = gives us a hint that we could use BFS
    #vertices: words (each word will be a node/vertex)
    #edges: link up the nodes that are only different by 1 letter (hit and hot only have 1 letter different, so we can connect them with an edge)

#HOW TO SOLVE ANY GRAPH PROBLEM (ALMOST!):
    # Read the problem, Translate it into a graph. (hardest part, requires a lot of thinking and creativity)
    # Build the graph. (adjacency list, or adjacency matrix)
    # Traverse the graph. 

# word_graph = {
#     'hit': {'hat', 'hot'},
#     'hat': {'cat', 'hot', 'hit'},
#     'cat': {'cot', 'hat'},
#     'hot': {''},
#     'cot': {},
#     'cog': {},
# }
# WE DON"T ACTUALLY NEED TO BUILD IT ALL OUT LIKE ABOVE. MOVE ON TO....

# I need the words.txt file that Artem has in his guided project. Then we would:
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

#Put our words in a set for O(1) lookup
word_set = set()
for word in words:
    word_set.add(word.lower())

def get_neigbors(word):
    # a neighbor is any word that's different by 1 letter 
    # and is inside word_list
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #all the way to z
    neighbors = set()
    string_word = list(word)

    for i in range(len(string_word)):
        for letter in letters:
            new_word = list(string_word)
            new_word[i] = letter
            new_word_string = "".join(new_word)
            if new_word_string != word and new_word_string in word_set:
                neighbors.add(new_word_string)
    return neighbors

    #Take each letter of alphabet (all 26 of them)
    #Generate EVERY combination of characters where we just change one letter at a time
    #Check that the word exists in word_list, and if it does,
    #it's a neighbor
    #Return all neighbors


class Queue():
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

def find_word_path(begin_word, end_word):
    #do BFS
    #create a queue
    #created a visited set
    #add start word to Queue (like a path)
    #while queue not empty
        #pop current word off queue
        #if word has not been visited:
            #is current word the end word? If yes, return path
            #add current word to visited set
            #add neighbors of current word to queue (like a path)
    queue = Queue()
    visited = set()
    queue.enqueue([begin_word])
    while queue.size() > 0:
        current_path = queue.dequeue()
        current_word = current_path[-1]
        if current_word not in visited:
            if current_word == end_word:
                return current_path
            visited.add(current_word)

            for neighbor_word in get_neighbors(current_word):
                #make a copy
                new_path = list(current_path)
                new_path.append(neighbor_word)
                queue.enqueue(new_path)

print(find_word_path('hit', 'cog'))            


