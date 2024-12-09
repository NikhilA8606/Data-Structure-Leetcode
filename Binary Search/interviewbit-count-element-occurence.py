https://www.interviewbit.com/problems/count-element-occurence/


class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return an integer
	def findCount(self, A, t):
        l = 0
        h = len(A)-1
        first = -1
        last = -1
        while l<=h:
            m = (l+h)//2
            if A[m]==t:
                first = m
                h = m - 1
            elif A[m]<t:
                l = m + 1
            else:
                h = m - 1
        l = 0
        h = len(A)-1
        while l<=h:
            m = (l+h)//2
            if A[m]==t:
                last = m
                l = m + 1
            elif A[m]<t:
                l = m + 1
            else:
                h = m - 1
        if first == -1 and last == -1:
            return 0
        else:
            return (last - first)+1
            
