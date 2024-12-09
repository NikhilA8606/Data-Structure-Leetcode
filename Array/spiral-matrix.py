54. Spiral Matrix

class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        t,l = 0,0
        b = n-1
        r = m-1
        lis = []
        while t<=b and l<=r:
            for i in range(l,r+1):
                lis.append(mat[t][i])
            t += 1
            for i in range(t,b+1):
                lis.append(mat[i][r])
            r -= 1
            if t<=b:
                for i in range(r,l-1,-1):
                    lis.append(mat[b][i])
                b -= 1
            if l<=r:
                for i in range(b,t-1,-1):
                    lis.append(mat[i][l])
                l += 1
        return lis

lis = [1,2,3]
for i in range(lis):
    print(i)
        
            
        