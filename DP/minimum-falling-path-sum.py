931. Minimum Falling Path Sum

class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        n = len(g)
        dp = [[0]*n for i in range(n)]
        for i in range(n):
            dp[0][i] = g[0][i]
        for i in range(1,n):
            for j in range(n):
                le = float("inf")
                ri = float("inf")
                if j-1>=0:
                    le = dp[i-1][j-1] + g[i][j]
                if j+1<n:
                    ri = dp[i-1][j+1] + g[i][j]
                do = dp[i-1][j] + g[i][j]
                dp[i][j] = min(le,ri,do)

        return min(dp[-1])

                
        