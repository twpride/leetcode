"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.

 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from pprint import pprint

class Solution:
  def pacificAtlantic(self, matrix):
    def dfs(r,c,thre):
      if mem[r][c] == thre: 
        return
      if mem[r][c] == -thre: 
        ans.append([r,c])
      mem[r][c] = thre

      for dr,dc in ((0,1),(0,-1),(-1,0),(1,0)):
        fr = r+dr
        fc = c+dc
        if (0<=fr<nr and 0<=fc<nc and matrix[fr][fc] >= matrix[r][c]):
          dfs(fr,fc,thre)

    ans = []
    nr = len(matrix)
    if not nr: return []
    nc = len(matrix[0])
    mem = [[0 for i in range(nc)] for j in range(nr)]
    
    for i in range(0, nr):
      dfs(i,0,1)
    for j in range(1, nc):
      dfs(0,j,1)
    for i in range(0, nr):
      dfs(i,nc-1,-1)
    for j in range(0, nc-1):
      dfs(nr-1,j,-1)

    return ans
import dis

s = Solution()
mat = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# mat = [[1,2],[4,3]]

y = dis.dis(s.pacificAtlantic)

print(y)