https://www.geeksforgeeks.org/problems/find-xor-of-numbers-from-l-to-r/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-xor-of-numbers-from-l-to-r

# You are given two integers L and R, your task is to find the XOR of elements of the range [L, R].

# Example:
# Input: 
# L = 4, R = 8 
# Output:
# 8 
# Explanation:
# 4 ^ 5 ^ 6 ^ 7 ^ 8 = 8

class Solution:
    def findXOR(self, l, r):
        def xor(n):
            if n % 4 == 1:
                return 1
            elif n % 4 == 2:
                return n + 1
            elif n % 4 == 3:
                return 0
            else:
                return n
        
        return xor(l-1) ^ xor(r)

