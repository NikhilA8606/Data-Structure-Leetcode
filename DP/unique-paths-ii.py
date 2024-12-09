63. Unique Paths II     

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        if g[0][0] == 1:
            return 0
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                up,left = 0,0
                if i==0 and j==0:
                    dp[i][j] = 1
                elif g[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i>0:
                        up = dp[i-1][j]
                    if j>0:
                        left = dp[i][j-1]
                    dp[i][j] = up + left
        return dp[m-1][n-1]
            

                        
                    

                    

        