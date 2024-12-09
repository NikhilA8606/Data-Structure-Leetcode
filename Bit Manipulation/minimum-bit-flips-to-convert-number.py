2220. Minimum Bit Flips to Convert Number

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        xor = start ^ goal
        c = 0
        while (xor!=0):
            xor = xor & (xor-1)
            c += 1
        return c

    
        