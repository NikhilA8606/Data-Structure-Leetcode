# https://www.geeksforgeeks.org/problems/subset-sums2234/1
# Subset Sums

class Solution:
	def subsetSums(self, arr, n):
	    sub = []
		def func(i,s,lis,l,ans):
		    if i==l:
		        ans.append(s)
		        return
		    func(i+1,s+lis[i],lis,l,ans)
		    func(i+1,s,lis,l,ans)
		
		func(0,0,arr,n,sub)
		return sub