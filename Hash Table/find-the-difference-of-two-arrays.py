2215. Find the Difference of Two Arrays

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        a=[]
        a=set(nums1) - set(nums2)
        b=[]
        b=set(nums2) - set(nums1)
        res.append(a)
        res.append(b)
        return res