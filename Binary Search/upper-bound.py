# Problem statement https://www.naukri.com/code360/problems/implement-upper-bound_8165383?utm_source=youtube&utm_medium=affiliate&utm_campaign=codestudio_Striver_BinarySeries&leftPanelTabValue=PROBLEM
# You are given a sorted array ‘arr’ containing ‘n’ integers and an integer ‘x’.Implement the ‘upper bound’ function to find the index of the upper bound of 'x' in the array.
# Note:
# 1. The upper bound in a sorted array is the index of the first value that is greater than a given value. 
# 2. If the greater value does not exist then the answer is 'n', Where 'n' is the size of the array.
# 3. Try to write a solution that runs in log(n) time complexity.

# Example:
# Input : ‘arr’ = {2,4,6,7} and ‘x’ = 5,
# Output: 2
# Explanation: The upper bound of 5 is 6 in the given array, which is at index 2 (0-indexed).

def upperBound(arr: [int], x: int, n: int) -> int:
    l,h = 0, len(arr)-1
    hb = len(arr)
    while(l<=h):
        m = (l+h)//2
        if arr[m]>x:
            hb = m
            h = m-1
        else:
            l = m+1
    return hb
    