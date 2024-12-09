120. Triangle

class Solution:
    def minimumTotal(self, t: List[List[int]]) -> int:
        n = len(t)
        dp = [[-1]*n for i in range(n)]
        for j in range(n):
            dp[n-1][j] = t[n-1][j]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                up = t[i][j] + dp[i+1][j]
                dia = t[i][j] + dp[i+1][j+1]
                
                dp[i][j] = min(up,dia)
        return dp[0][0]
        