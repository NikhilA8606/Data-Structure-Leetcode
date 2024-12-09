# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        h = x
        r = 0
        while l<=h:
            m = (l+h)//2
            if m*m<=x:
                r = m
                l = m + 1
            else:
                h = m - 1
        return r
        