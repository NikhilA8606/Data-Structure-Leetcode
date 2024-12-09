1004. Max Consecutive Ones III

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j,c,res = 0,0,0,0
        while j<len(nums):
            if nums[j]==0:
                c += 1
            if c<=k:
                res = max(j-i+1,res)
                j += 1
            else:
                if nums[i]==0:
                    c -= 1
                i += 1
                j += 1      
        return res

        