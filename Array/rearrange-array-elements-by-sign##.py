2149. Rearrange Array Elements by Sign

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        lis = [0] * len(nums)
        p = 0
        n = 1

        for i in nums:
            if i>0:
                lis[p] = i
                p += 2
            else:
                lis[n] = i
                n += 2
        return lis
                
