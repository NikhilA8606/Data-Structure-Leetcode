73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, mat: List[List[int]]) -> None:
        m = len(mat)
        n = len(mat[0])

        t = []
        v = []

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    t.append(j)
                    v.append(i)

        for i in range(m):
            for j in range(n):
                if i in v or j in t:
                    mat[i][j] = 0
                
        return mat
        