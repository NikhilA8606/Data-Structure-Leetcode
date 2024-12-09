https://www.interviewbit.com/problems/redundant-braces/

class Solution:
	# @param A : string
	# @return an integer
	def braces(self, A):
		stack = []
		for i in A:
			if i == ')':
				top = stack.pop()
				ele = 0
				while top != '(':
					if top in '+*-/':
						ele += 1
					top = stack.pop()
				
				if ele == 0:
					return 1
			else:
				stack.append(i)
		return 0
