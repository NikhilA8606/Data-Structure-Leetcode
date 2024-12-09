75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        r = nums.count(0)
        b = nums.count(1)
        c = nums.count(2)
        for i in range(len(nums)):
            if r > 0:
                nums[i] = 0
                r -= 1
            elif b > 0:
                nums[i] = 1
                b -= 1
            elif c > 0:
                nums[i] = 2
                c -= 1
        return nums
        
        