# https://www.naukri.com/code360/problems/total-unique-paths_1081470?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&count=25&page=1&search=&sort_entity=order&sort_order=ASC&leftPanelTabValue=SUBMISSION
#  Unique Paths

def uniquePaths(m, n):
	dp = [[-1]*n for j in range(m)]
	dp[0][0] = 1
	for i in range(m):
		for j in range(n):
			if i==0 and j==0:
				continue
			up,left = 0,0
			if i>0:
				up = dp[i-1][j]
			if j>0:
				left = dp[i][j-1]
			dp[i][j] = up + left
	return dp[m-1][n-1]