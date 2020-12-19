class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        memo=[[-1 for _ in range(n)] for _ in range(m)]
        
        def dfs(i,j):
            if memo[i][j]!=-1:
                return memo[i][j]
            if i==m-1 or j==n-1:
                return 1
            else:
                memo[i][j]=dfs(i+1,j)+dfs(i,j+1)
            
            return memo[i][j]

        return dfs(0,0) 


        
class Solution: #bottom up
    def uniquePaths(self, m: int, n: int) -> int:
        if n>m:
          n,m=m,n
        
        grid=[[-1 for j in range(n)] for i in range(m)]       
        
        for k in range(m):
          grid[k][-1]=1
        
        for i in range(1,n):
          grid[m-i][n-i-1]=grid[m-i-1][n-i]

          for j in range(i,m):
            grid[m-j-1][n-i-1]=grid[m-j][n-i-1]+grid[m-j-1][n-i]

            
        return grid[0][0]