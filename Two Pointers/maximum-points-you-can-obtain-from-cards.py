1423. Maximum Points You Can Obtain from Cards

class Solution:
    def maxScore(self, c: List[int], k: int) -> int:
        lsum = sum(c[:k])
        res = lsum
        rsum = 0
        i = k-1
        j = len(c)-1
        while i>=0:
            lsum -= c[i]
            rsum +=  c[j]
            res = max(lsum+rsum,res)
            i -= 1
            j -= 1
        return res

        