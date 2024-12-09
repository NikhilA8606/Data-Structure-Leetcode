https://www.geeksforgeeks.org/problems/minimal-cost/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimal-cost


class Solution:
    def minimizeCost(self, arr, k):
        n = len(arr)
        dp = [0 for i in range(n)]
        for i in range(1,n):
            mini = float("inf")
            for j in range(1,k+1):
                if i-j >= 0:
                    jump = dp[i-j] + abs(arr[i] - arr[i-j])
                    mini = min(mini,jump)
            dp[i] = mini
        return dp[n-1]