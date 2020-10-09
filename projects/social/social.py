import random
import math
from collections import deque

class User:
    def __init__(self, name):
        self.name = name
#class User, takes in a name

#Bi-directional edges
#If A is friends with B, B is friends with A

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        #Maps IDs to User objects (lookup table for User Objects given IDs)
        self.users = {} # {1: User("1"), 2: User("2"), ...}
        #Adjacency List
        #Maps user_ids to a list of other users (who are their friends)
        self.friendships = {} # {1: {2, 3, 4}, 2: {1}, 3: {1}, 4: {1}} example

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            #print("WARNING: You cannot be friends with yourself")
            return False #if add friendship fails, return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            #print("WARNING: Friendship already exists")
            return False

        self.friendships[user_id].add(friend_id)
        self.friendships[friend_id].add(user_id)
        return True

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name) #mapping user to user object {1: User("mari")}
        self.friendships[self.last_id] = set() #brand new user doesn't have any friends yet {1: {}}

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        #RUNTIME of populate_graph is On^2 because of double For Loop

        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        #Add users in range from 0 to num_users
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships    
        # Generate all possible friendships and put them in an array
        # 3 users with ids (0, 1, 2)
        # for example 0 is friends with 1, 0 is friends with 2, 1 is friends with 2 -->  [(0, 1), (0, 2), (1, 2)]
        possible_friendships = []
        
        for user_id in self.users:
            #To prevent duplicate friendships, created user_id + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        
        #Randomly select X friendships
        #The formula for X is num_users * avg_friendships // 2
        # Shuffle friendship array in random order
        random.shuffle(possible_friendships)

        # Take the first num_users * avg_friendships / 2 and that will be the friendships for that graph

        #x = 0
        for i in range(0, math.floor(num_users * avg_friendships / 2)):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1]) #pass in IDs of both users who are becoming friends, helper method creates friendship edge
    
    def populate_graph_linear(self, num_users, avg_friendships):
        #Keep randomly making friendships until we've made the right amount
        #Randomly select two vertices to become friends
        #If it is a success, then increment number of friendships made
        #Else, try again
    
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        for i in range(0, num_users):
            self.add_user(f"User {i}")

        target_friendships = num_users * avg_friendships
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship_linear(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f"collisions: {collisions}")


    def add_friendship_linear(self, user_id, friend_id):
        if user_id == friend_id:
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)



    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        #this will map from node id --> [path from user_id]
        visited = {}  # Note that this is a dictionary, not a set

        # !!!! IMPLEMENT ME
        #Return user's extended social network and chain of friendships that link them
        #Travers through graph wtih BFS (because we need SHORTEST path from one node to another)
        #Keep track of results with the visited dictionary

        queue = deque() #need this for BFT
        queue.append([user_id])
        while len(queue) > 0:
            currPath = queue.popleft()
            currNode = currPath[-1] #current path is last item in that path
            visited[currNode] = currPath #bft guarantees that this is shortest path to currNode from user_id
            for friend in self.friendships[currNode]:
                if friend not in visited:
                    newPath = currPath.copy()
                    newPath.append(friend)
                    queue.append(newPath)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(f"friendships: {sg.friendships}")
    connections = sg.get_all_social_paths(1)
    print(f"connections: {connections}")
