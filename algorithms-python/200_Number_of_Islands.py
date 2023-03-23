'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col):
            grid[row][col]="2"

            if row-1 >= 0 and grid[row-1][col] == "1":
                bfs(row-1,col)
            if row+1 < len(grid) and grid[row+1][col] == "1":
                bfs(row+1,col)
            if col-1 >= 0 and grid[row][col-1] == "1":
                bfs(row,col-1)
            if col+1 < len(grid[row]) and grid[row][col+1] == "1":
                bfs(row,col+1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    counter+=1
                    bfs(i,j)
        
        return counter