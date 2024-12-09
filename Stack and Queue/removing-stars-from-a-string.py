class Solution:
    def removeStars(self, s: str) -> str:
        lis = []
        for i in s:
            if i == '*':
                lis.pop()
            else:
                lis.append(i)
        return ''.join(lis)
        