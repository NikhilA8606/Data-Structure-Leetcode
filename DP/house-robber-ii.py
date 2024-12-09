213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        def answer(lis):
            dp = [0 for _ in range(len(lis))]
            dp[0] = lis[0]
            for i in range(1,len(lis)):
                if i-2>=0:
                    take = lis[i] + dp[i-2]
                else:
                    take = lis[i]
                nontake = dp[i-1]
                dp[i] = max(take,nontake)
            return dp[len(lis)-1]
        temp1 = nums[:n-1]
        temp2 = nums[1:]
        return max(answer(temp1),answer(temp2))
    
    
    
    