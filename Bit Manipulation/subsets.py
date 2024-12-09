78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(2**n):
            lis = []
            for j in range(n):
                if i & (1<<j):
                    lis.append(nums[j])
            res.append(lis)
        return res       