1679. Max Number of K-Sum Pairs  

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()           # can be more efficient by using hashmap            
        i = 0
        j = len(nums)-1
        c = 0
        while i<j:
            sum = nums[i] + nums[j]
            if sum == k:
                c += 1
                i += 1
                j -= 1
            elif sum<k:
                i += 1
            else:
                j -= 1
        return c


        