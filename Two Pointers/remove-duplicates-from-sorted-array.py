26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        l = 0
        r = 1
        while r < n:
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
            r += 1
        return l + 1
        