201. Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, l: int, r: int) -> int:
        s = 0
        while l<r:
            l >>= 1
            r >>= 1
            s += 1
        return l<<s