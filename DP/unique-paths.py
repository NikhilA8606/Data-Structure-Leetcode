62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                up = 0
                left = 0
                if i==0 and j == 0:
                    dp[i][j] = 1
                else:
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[m-1][n-1]
            
        
