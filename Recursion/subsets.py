78. Subsets

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        def ans(i,temp):
            if i == n:
                result.append(temp[:])  #store the copy of the temp to result because temp will be changed in the next
                return
            temp.append(nums[i])
            ans(i+1,temp)
            temp.pop()
            ans(i+1,temp)
        ans(0,[])
        return result
        
        
        