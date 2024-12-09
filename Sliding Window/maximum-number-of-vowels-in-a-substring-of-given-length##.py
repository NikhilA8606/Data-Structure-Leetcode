1456. Maximum Number of Vowels in a Substring of Given Length

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        i, j, c, res = 0, 0, 0, 0
        v = {'a', 'e', 'i', 'o', 'u'}
        while j < len(s):
            if s[j] in v:
                c += 1
            if j - i + 1 == k:
                res = max(res, c)
                if s[i] in v:
                    c -= 1
                i += 1
            j += 1
        return res
