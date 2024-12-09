128. Longest Consecutive Sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 1
        if not nums:
            return 0
        num_set = set(nums)
        for i in num_set:        
            if i-1 not in num_set:
                val = i +1
                c = 1
                while val in num_set:
                    c += 1
                    val += 1
                max_len = max(c,max_len)
        return max_len
            



        