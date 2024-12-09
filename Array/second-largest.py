# https://www.geeksforgeeks.org/problems/second-largest3735/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=second-largest

# Given an array arr of size n, print the second largest distinct element from an array. If the second largest element doesn't exist then return -1.

class Solution:
	def print2largest(self,a, n):
		l = a[0]
		s_l = -1
		for i in range(n):
		    if a[i] > l:
		        s_l = l
		        l = a[i]
		    elif a[i] < l and a[i] > s_l:
		        s_l = a[i]
		return s_l