# Max Sum Subarray of size K
# Given an array of integers Arr of size N and a number K. Return the maximum sum of a subarray of size K.
# Input:
# N = 4, K = 2
# Arr = [100, 200, 300, 400]
# Output:
# 700
# Explanation:
# Arr3  + Arr4 =700,
# which is maximum.

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        i = 0
        sum = 0
        res = 0
        for j in range(N):
            sum += Arr[j]
            if j-i+1==K:
                res = max(res,sum)
                sum -= Arr[i]
                i += 1
        return res
