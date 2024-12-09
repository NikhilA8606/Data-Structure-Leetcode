229. Majority Element II

import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        s = set()
        t = math.floor(len(nums)/3)
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
            if dic[i] > t:
                s.add(i)
        return list(s)
        