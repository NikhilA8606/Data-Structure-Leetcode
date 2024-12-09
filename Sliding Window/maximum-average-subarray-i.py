643. Maximum Average Subarray I

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i,j,s,avg = 0,0,0,0
        res = float('-inf')
        while j<len(nums):
            s += nums[j]
            if j-i+1==k:
                avg = s/k
                res = max(avg,res)
                s -= nums[i]
                i += 1
            j += 1
        return res
        