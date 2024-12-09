72. Edit Distance

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        d = [[0 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            d[i][0] = i
        for i in range(n+1):
            d[0][i] = i
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    d[i][j] = d[i-1][j-1]
                else:
                    d[i][j] = min(d[i-1][j],d[i-1][j-1],d[i][j-1]) + 1
        return d[m][n]

#  i,j = m,n
    
#     while(i>0 and j>0):

#         if w1[i-1]==w2[j-1]:
#             i-=1
#             j-=1
#         elif d[i][j] == 1+d[i-1][j]:
#             print(f"deleted {w1[i-1]}")
#             i-=1
#         elif d[i][j] == 1+d[i][j-1]:
#             print(f"inserted {w2[j-1]}")
#             j-=1
#         else:
#             print(f"substituted {w1[i-1]} with {w2[j-1]}")
#             i-=1
#             j-=1


                
        