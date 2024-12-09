# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, a: List[List[int]], t: int) -> bool:
        n = len(a)
        m = len(a[0])
        l = 0
        h = (n*m)-1
        while l<=h:
            mid = (l+h)//2
            i = mid//m
            j = mid%m
            if a[i][j]==t:
                return True
            elif a[i][j]>t:
                h = mid - 1
            else:
                l = mid + 1
        return False        