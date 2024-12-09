https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
# Given a string you need to print the size of the longest possible substring that has exactly K unique characters. If there is no possible substring then print -1.
# Example 1:
# Input:
# S = "aabacbebebe", K = 3
# Output: 
# 7
# Explanation: 
# "cbebebe" is the longest substring with 3 distinct characters.

class Solution:

    def longestKSubstr(self, s, k):
        dic = {}
        i,res = 0,-1
        for j in range(len(s)):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            while len(dic)>k:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    dic.pop(s[i])
                i += 1
            if len(dic)==k:
                res = max(res,j-i+1)

        return res

