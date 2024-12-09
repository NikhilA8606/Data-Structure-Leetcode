# https://www.interviewbit.com/problems/pair-with-given-difference/
# Pair With Given Difference


class Solution:
    def solve(self, A, B):
        l = 0
        r = 1
        A.sort()
        while l < len(A) and r < len(A):
            if l != r and A[r] - A[l] == B:
                return 1
            elif A[r] - A[l] < B:
                r += 1
            else:
                l += 1
        
        return 0