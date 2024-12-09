88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if not nums1:
            return nums2
        if not nums2:
            return nums1
        e = len(nums1)-1
        while m > 0 and n > 0:
            if nums1[m-1]>nums2[n-1]:
                nums1[e] = nums1[m-1]
                m -= 1
            else:
                nums1[e] = nums2[n-1]
                n -= 1
            e -= 1
       
        while n>0:
            nums1[e] = nums2[n-1]
            n -= 1
            e -= 1
        return nums1