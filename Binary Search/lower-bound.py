# Coding ninjas : https://www.naukri.com/code360/problems/lower-bound_8165382?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=PROBLEM
# Problem statement
# You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.
# Note:
# 1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.
# 2. Try to do this in O(log(n)).

# Example:
# Input: ‘arr’ = [1, 2, 2, 3] and 'x' = 0
# Output: 0
# Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.

def lowerBound(arr: [int], n: int, x: int) -> int:
    l = 0
    h = len(arr)-1
    lb = len(arr)
    while l<=h:
        m = (l+h)//2
        if arr[m]>=x:
            lb = m  
            h = m-1
        else:
            l = m+1
    return lb
    
