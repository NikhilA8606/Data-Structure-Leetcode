# https://www.naukri.com/code360/problems/minimum-path-sum_985349?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION
#  Minimum Path Sum

n=3
m=3
grid = [[0,2,3],[1,3,2],[1,1,0]]

def maxSumPath(grid):
    dp = [[-1]*m for i in range(n)]
    dp[0][0] = grid[0][0]
    last = dp[0][0]
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            up = float("-inf")
            left = float("-inf")
            if i > 0:
                up = grid[i][j] + dp[i-1][j]
            if j>0:
                left = grid[i][j] + dp[i][j-1]
            dp[i][j] = max(up,left)
    s = 0
    for i in range(n):
        s += dp[i][m-1]
    return dp[n-1][m-1]
print(maxSumPath(grid))