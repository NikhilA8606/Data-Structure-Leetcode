202. Happy Number

class Solution:
    def isHappy(self, num: int) -> bool:
        if num == 1:
            return True
        lis = []
        while num > 0:
            lis.append(num)
            n = num
            s = 0
            while n>0:
                r = n % 10
                s += r ** 2
                n = n // 10
            if s in lis:
                return False
            elif s == 1:
                return True
            num = s

        