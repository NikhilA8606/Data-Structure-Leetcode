https://www.interviewbit.com/problems/search-in-bitonic-array/

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        a = max(A)
        i = A.index(a)
        if a==B:
            return i
        def increase(arr,p,t):
            l = 0
            h = p
            while l<=h:
                m = (l+h)//2
                if A[m]==t:
                    return m
                elif t<A[m]:
                    h = m -1
                else:
                    l = m + 1
            return -1
        def decreas(arr,p,t):
            l = p
            h = len(A)-1
            while l<=h:
                m = (l+h)//2
                if A[m]==B:
                    return m
                elif B<A[m]:
                    l = m + 1
                else:
                    h = m - 1
            return -1
        if increase(A,i-1,B) != -1:
            return increase(A,i-1,B)
        return decreas(A,i+1,B)
                
        
                    
                    
        
        
            
            
