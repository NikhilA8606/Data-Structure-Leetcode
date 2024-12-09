# 153. Find Minimum in Rotated Sorted Array

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        mi = 2**31 - 1
        while l<=h:
            m = (l+h)//2
            if nums[m]>=nums[l]:
                mi = min(mi,nums[l])
                l = m + 1
            else:
                mi = min(mi,nums[m])
                h = m - 1
        return mi
        