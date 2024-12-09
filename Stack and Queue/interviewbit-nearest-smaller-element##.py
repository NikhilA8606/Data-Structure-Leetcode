https://www.interviewbit.com/problems/nearest-smaller-element/

from collections import defaultdict
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def prevSmaller(self, A):
        res = []
        stack = []
        for i in A:
            while stack and i <= stack[-1]:
                stack.pop()
            
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            
            stack.append(i)
        return res
                    
            
                
                
                    
                
                
        
