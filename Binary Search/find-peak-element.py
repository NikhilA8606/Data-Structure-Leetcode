# 162. Find Peak Element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1 or nums[0]>nums[1]:
            return 0
        if nums[n-1]>nums[n-2]:
            return n-1
        l = 1
        h = n-2
        while l<=h:
            mid = (l+h)//2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid]>nums[mid-1]:
                l = mid + 1
            elif nums[mid]<nums[mid-1]:
                h = mid - 1
            else:
                 l = mid + 1 #it means the mid at reverse peak possition  
        return -1
        
        