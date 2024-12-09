# Colorful Number
# https://www.interviewbit.com/problems/colorful-number/

class Solution:
	# @param A : integer
	# @return an integer
	def colorful(self, B):
		lis = list(str(B))
        res = []
        for i in range(len(lis)):
            p = int(lis[i])
            for j in range(i,len(lis)):
                if i == j:
                    if p not in res:
                        res.append(int(p))
                    else:
                        return 0
                else: 
                    p = p * int(lis[j])
                    if p in res:
                        return 0
                res.append(p)
        return 1
                    
                    
            
			
		

			
		
