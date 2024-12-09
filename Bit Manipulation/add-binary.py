67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = int(a,2)
        num2 = int(b,2)
        s = num1 + num2
        if s == 0:
            return "0"
        res = ""
        while s != 1:
            if s & 1 == 1:
                res += '1'
            else:
                res += '0'
            s = s >> 1
        res += '1'
        return ''.join(reversed(res))
    