1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        d = [[0 for j in range(n+1)] for i in range(m+1)]
        
        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    d[i][j] = 1 + d[i-1][j-1]
                else:
                    d[i][j] = max(d[i-1][j],d[i][j-1])
        return d[m][n]
        
    

    # i,j = n,m
    # ans = ""
    # while(i>0 and j>0):
    #     if word2[i-1]== word1[j-1]:
    #         ans = ans+word2[i-1]
    #         i-=1
    #         j-=1
    #     elif d[i-1][j] >= d[i][j-1]:
    #         i-=1    
    #     else:
    #         j-=1

    # print(ans[::-1])
