90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result=[]
        def ans(i,temp):
            if i == n:
                if temp not in result:
                    result.append(temp[:])   
                return
            temp.append(nums[i])
            ans(i+1,temp)
            temp.pop()
            ans(i+1,temp)
        ans(0,[])
        return result