# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        n = len(a)
        m = len(a[0])
        r = 0
        c = m-1
        while r<n and c>=0:
            if a[r][c]==t:
                return True
            elif a[r][c]>t:
                c = c - 1
            else:
                r = r + 1
        return False
    




            
        