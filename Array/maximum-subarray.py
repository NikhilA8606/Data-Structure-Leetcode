53. Maximum Subarray ('kadane's algorithm)

class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        s = 0
        max_sum = A[0]
        for i in range(len(A)):
            s = s + A[i]
            if max_sum<s:
                max_sum = s   
            if s<0:
                s = 0
        return max_sum
        