438. Find All Anagrams in a String
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = {}
        res = []
        i = 0
        count = Counter(p)
        for j in range(len(s)):
            if s[j] not in dic:
                dic[s[j]] = 0
            dic[s[j]] += 1
            if j-i+1 == len(p):
                if dic == count:
                    res.append(i)
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    dic.pop(s[i])
                i+=1
        return res
            

