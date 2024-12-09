198. House Robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        for i in range(1,n):
            if i-2>=0:
                take = nums[i] + dp[i-2]
            else:
                take = nums[i]
            nontake = dp[i-1]
            dp[i] = max(take,nontake)
        return dp[n-1]
        