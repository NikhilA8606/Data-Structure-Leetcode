# https://www.geeksforgeeks.org/problems/count-occurences-of-anagrams5839/1
# Given a word pat and a text txt. Return the count of the occurrences of anagrams of the word in the text.

# Example 1:

# Input:
# txt = forxxorfxdofr
# pat = for
# Output: 3
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.

from collections import Counter#User function Template for python3
class Solution:

	
	def search(self,pat, s):
	    count = Counter(pat)
	    dic = {}
	    c = 0
	    i = 0
	    for j in range(len(s)):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            if j-i+1 == len(pat):
                if dic == count:
                    c += 1
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    dic.pop(s[i])
                i+=1
        return c
