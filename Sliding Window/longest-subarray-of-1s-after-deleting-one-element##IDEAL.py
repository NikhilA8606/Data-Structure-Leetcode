1493. Longest Subarray of 1's After Deleting One Element

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        c = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                c += 1
            while c > 1:
                if nums[i] == 0:
                    c -= 1
                i += 1
            res = max(res, j - i)
        return res


#1004 Max Consecutive Ones III are similar to each other

