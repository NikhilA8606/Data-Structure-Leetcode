https://www.interviewbit.com/problems/trailing-zeroes/

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        c = 0
        while A != 0:
            if A & 1 == 0:
                c += 1
            else:
                break
            A = A>>1
        return c 
