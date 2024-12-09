137. Single Number II

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for i in nums:
            ones = (ones ^ i) & (~twos)
            twos = (twos ^ i) & (~ones)
        return ones

# Brute Force:
# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in range(1,len(nums),3):
#             if nums[i] != nums[i-1]:
#                 return nums[i-1]
#         return nums[len(nums)-1]
        