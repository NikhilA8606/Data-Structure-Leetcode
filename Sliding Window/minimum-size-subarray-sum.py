# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a 
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, t: int, nums: List[int]) -> int:
        if sum(nums)<t:
            return 0
        res,s,i = len(nums),0,0
        for j in range(len(nums)):
            s += nums[j]
            while s>=t:
                res = min(res,j-i+1)
                s -= nums[i]
                i += 1
        return res
        