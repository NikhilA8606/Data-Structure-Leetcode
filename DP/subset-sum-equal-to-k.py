https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954?leftPanelTab=1%3Fsource%3Dyoutube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=SUBMISSION
# Subset Sum Equal to K

from os import *
from sys import *
from collections import *
from math import *

def subsetSumToK(n, k, arr):
    # Initialize the dp array with False
    dp = [[False] * (k + 1) for _ in range(n)]
    
    # Base Case: Sum of 0 is always possible
    for i in range(n):
        dp[i][0] = True
    
    # If the first element is less than or equal to k, mark it
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    # Fill the dp array
    for i in range(1, n):
        for j in range(1, k + 1):
            nontake = dp[i - 1][j]
            take = False
            if arr[i] <= j:
                take = dp[i - 1][j - arr[i]]
            dp[i][j] = take or nontake
    
    # Return if the subset sum to k is possible
    return dp[n - 1][k]

Reccursion Answer

func (i,t)
{
    if t == 0:
        return True
    if i == 0:
        return t == a[i]
    nontake = func(i-1,t)
    take = False
    if t>=a[i]:
        take = func(i-1,t-a[i])
    return take or nontake
}
