29. Divide Two Integers

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:   #special overflow case
            return 2147483647
        add = 0
        divid = abs(dividend)
        divis = abs(divisor)
        while divid >= divis:
            s = 0
            i = 0
            while divis << (i + 1) <= divid:
                i += 1
            add += 1 << i
            divid = divid - (divis * (1 << i))
        if dividend < 0 and divisor < 0:
            return add
        elif dividend < 0 or divisor < 0:
            return (0-add)
        else:
            return add        
        

            
        