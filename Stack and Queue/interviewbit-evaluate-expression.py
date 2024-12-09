https://www.interviewbit.com/problems/evaluate-expression/

class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        stack = []
        for i in A:
            if i in '*/+-':
                b = int(stack.pop())
                a = int(stack.pop())
                
                if i == '*':
                    stack.append(a*b)
                elif i == '+':
                    stack.append(a+b)
                elif i == '-':
                    stack.append(a-b)
                elif i == '/':
                    stack.append(int(a/b))
            else:
                stack.append(i)
        return stack[-1]