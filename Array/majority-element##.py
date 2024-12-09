169. Majority Element

import math
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):
            if c == 0:
                c += 1
                ele = nums[i]
            elif nums[i] == ele:
                c += 1
            elif nums[i] != ele:
                c -= 1
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == ele:
                cnt += 1
            if cnt > len(nums)/2:
                return ele
        return -1

       