338. Counting Bits 

class Solution:
    def countBits(self, n: int) -> List[int]:
        lis = []
        for i in range(n+1):
            c = 0
            while i != 0:
                i = i & (i-1)
                c += 1
            lis.append(c)
        return lis
        