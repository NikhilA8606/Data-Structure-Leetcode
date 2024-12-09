118. Pascal's Triangle

class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]*i for i in range(1,n+1)]

        for i in range(n):
            for j in range(i):
                if j != 0 and j != i:
                    ans[i][j] = ans[i-1][j-1] + ans[i-1][j]
        return ans