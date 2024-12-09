496. Next Greater Element I

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        dic = {}
        for i in range(len(nums2)-1,-1,-1):
            while stack and nums2[i] >= stack[-1]:
                stack.pop()
            if stack:
                dic[nums2[i]] = stack[-1]
            else:
                dic[nums2[i]] = -1
            stack.append(nums2[i])

        res = [dic[num] for num in nums1]
        return res
            
        