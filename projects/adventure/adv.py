from room import Room
from player import Player
from world import World
from queue import Queue
# from collections import deque

import random
from ast import literal_eval

# Load world
world = World()

'''
Notes:
vertex = room
edges = paths between rooms

Keys = room id
Values = direction towards next room (?)

DFT to explore through rooms
BFS to backtrack and find open, unvisited room
    BFS returns a PATH
    Move player down the path

get_exits: gets the room and directions to figure out where to go next

Keep visited set so that don't go to same room again.
'''

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

#traversal_path = []

def get_maze_path():
    #save rooms in dictionary
    rooms = {}

    #Traverse through rooms starting at current_room of 0
    #Keep track of the visited rooms in an empty set, initialize visited to None
    def dft(current_room, visited=None):
        #base case is if visited is None, assign the visited variable to an empty set
        if visited == None:
            visited = set()
        elif current_room.id in visited:
            return visited
        print(current_room.name, current_room.get_coords())

        #add the current room's id to the visited set
        visited.add(current_room.id)

        rooms[current_room.id] = {}
        print(visited)

        for direction in current_room.get_exits():
            next_room = current_room.get_room_in_direction(direction)
            rooms[current_room.id][direction] = next_room.id 
            dft(next_room, visited)
            #print(next_room)

    def bfs(starting_room_id, destination_room_id):
        #FIFO, take first "starting_room" from queue, check if it was visited or not, check if it is the destination room/goal, put all neighbors at the end of the queue, repeat
        q = Queue()
        q.put([starting_room_id])
        visited = set()

        while not q.empty():
            path = q.get()
            #start at the end of the queue/path (the last move, now going backwards)
            current_room_id = path[-1]

            #if current room has been visited, skip and continue on
            if current_room_id in visited:
                continue
            
            #if current room is the "goal" then return the path
            if current_room_id == destination_room_id:
                return path
            
            #add the current room to the visited set
            visited.add(current_room_id)

            #put item into the queue
            for room_id in rooms[current_room_id].values():
                q.put(path + [room_id])
    
    #Traverse graph, filling rooms with directions and room_ids
    dft(player.current_room)
    
    #for easier reference, assign ids to a list of the rooms
    ids = list(rooms.keys())
    #print(ids)
    
    #empty array for the traversal path that will soon be added to
    traversal_path = []

    #iterate through the list of room ids
    for i in range(len(ids) - 1):
        #start bfs to set the path from first id to next id
        path = bfs(ids[i], ids[i + 1])

        #iterate through the path
        #append direction to traversal_path array
        for j in range(len(path) - 1):
            cur_room_id, next_room_id = path[j], path[j + 1]
            for direction, room_id in rooms[cur_room_id].items():
                if room_id == next_room_id:
                    traversal_path.append(direction)

    print(traversal_path)
    print(len(traversal_path))
    print(rooms)
    return traversal_path

traversal_path = get_maze_path()


# TRAVERSAL TEST -- DO NOT MODIFY THIS
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")




    # def dft(current_room):
    #     stack = deque()
    #     visited = set()
    #     stack.append(current_room.id)
        
    #     while len(stack) > 0:
    #         current_room.id = stack.pop()

    #         if current_room.id not in visited:
    #             print(current_room.id)
    #             visited.add(current_room.id)

    #             rooms[current_room.id] = {}
    #             exits = current_room.get_exits()
    #             for direction in exits:
    #                 neighbor = current_room.get_room_in_direction(direction)
    #                 rooms[current_room.id][direction] = neighbor.id 
    #                 stack.append(neighbor)