34. Find First and Last Position of Element in Sorted Array
class Solution:
    def searchRange(self, nums: List[int], t: int) -> List[int]:
        l = 0
        h = len(nums)-1
        first = -1
        last = -1
        while l<=h:
            m = (l+h)//2
            if nums[m]==t:
                first = m
                h = m - 1
            elif nums[m]<t:
                l = m + 1
            else:
                h = m - 1
        l = 0
        h = len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m]==t:
                last = m
                l = m + 1
            elif nums[m]<t:
                l = m + 1
            else:
                h = m - 1
        return [first,last]
        