# https://www.naukri.com/code360/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=SUBMISSION

from typing import List

MOD = 10**9 + 7

def findWays(arr: List[int], k: int) -> int:
    n = len(arr)
    
    # Initialize DP table with 0
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Base case: There's exactly one way to get a sum of 0 (by choosing no elements)
    for i in range(n):
        dp[i][0] = 1
    
    # If the first element is <= k, set dp[0][arr[0]] = 1
    if arr[0] <= k:
        dp[0][arr[0]] = 1
    
    # Fill the DP table
    for i in range(1, n):
        for j in range(k + 1):
            # Non-pick case: Exclude current element
            nonpick = dp[i - 1][j]
            
            # Pick case: Include current element if it can contribute to the sum
            pick = 0
            if arr[i] <= j:
                pick = dp[i - 1][j - arr[i]]
            
            # Total ways: Sum of pick and non-pick cases, taken modulo MOD
            dp[i][j] = (pick + nonpick) % MOD
    
    # The answer is the number of ways to get sum 'k' using all elements
    return dp[n - 1][k]
