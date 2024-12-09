# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        i,res = 0,0
        for j in range(len(s)):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            while len(dic)<j-i+1:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    dic.pop(s[i])
                i += 1
            res = max(res,j-i+1)
        return res

        