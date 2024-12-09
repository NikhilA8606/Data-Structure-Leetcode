283. Move Zeroes


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        if n<2:
            return nums
        l,r = 0,1
        while(r<n):
            if nums[l] != 0:
                l += 1
                r += 1
            elif nums[r] == 0:
                r += 1
            else:
                nums[l] = nums[r]
                nums[r] = 0
        return nums
        
        
        