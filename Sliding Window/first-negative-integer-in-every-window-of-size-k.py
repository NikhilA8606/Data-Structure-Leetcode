# First negative integer in every window of size k
# Given an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.
https://www.geeksforgeeks.org/problems/first-negative-integer-in-every-window-of-size-k3345/1
# Example 1:

# Input : 
# N = 5
# A[] = {-8, 2, 3, -6, 10}
# K = 2
# Output : 
# -8 0 -6 -6
# Explanation :
# First negative integer for each window of size k
# {-8, 2} = -8
# {2, 3} = 0 (does not contain a negative integer)
# {3, -6} = -6
# {-6, 10} = -6

def printFirstNegativeInteger( A, N, K):
    i = 0
    res = []
    for j in range(len(A)):
        flag = 0
        if j-i+1==K:
            k = i
            while k<=j:
                if A[k]<0:
                    res.append(A[k])
                    flag = 1
                    break
                k += 1
            i += 1
            
            if flag==0:
                res.append(0)
    return res


