"""
Leetcode Problem: leetcode.com/problems/number-of-islands

Problem:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Plan
1. Translate the problem into graph terminology
vertex - is a cell
edge - neighboring cells

2. Build graph
we already have a graph given in the grid matrix!

3. Traverse graph/grid
go through each element in the grid
if we find a 1:
increment numIslands
    then we want to traverse all of its connected components
and mark them as visited
return numIslands

"""
from collections import deque

class Solution:
    #initialize numIslands at 0, then keep count by incrementing += 1
    numIslandsFound = 0
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        width, height = len(grid[0]), len(grid)
        visited = [[False] * width for x in range(height)]
        for y in range(height):
            for x in range(width):
                if grid[y][x] == '1' and not visited[y][x]:
                    self.numIslandsFound += 1
                    self.markConnectedComponentsAsVisited(grid, visited, x, y)
        return self.numIslandsFound
    
    #Start at x,y and mark connected components as 1 if they are visited
    def markConnectedComponentsAsVisited(self, grid, visited, x, y):
        #now do a traversal, marking visited cells
        width, height = len(grid[0]), len(grid)
        stack = deque()
        stack.append((x, y))
        while len(stack) > 0:
            x, y = stack.pop()
            if visited[y][x]:
                continue
            visited[y][x] = True
            #Traverse all adjacent nodes that are also 1
            #Check left node
            if x - 1 >= 0 and grid[y][x - 1] == '1':
                stack.append((x - 1, y))
            #Check right node
            if x + 1 < width and grid[y][x + 1] == '1':
                stack.append((x + 1, y))
            #Check top node
            if y - 1 >= 0 and grid[y - 1][x] == '1':
                stack.append((x, y - 1))
            #Check bottom node
            if y + 1 < height and grid[y + 1][x] == '1':
                stack.append((x, y + 1))