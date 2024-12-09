Sorted Insert Position

https://www.interviewbit.com/problems/sorted-insert-position/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        l = 0
        h = len(A)-1
        up = -1
        while l<=h:
            m = (l+h)//2
            if A[m] == B:
                return m
            elif A[m]>B:
                up = m
                h = m - 1
            else:
                l = m + 1
        if up == -1:
            return len(A)
        else:
            return up
            
