# 2352. Equal Row and Column Pairs

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic = defaultdict(int)
        c = 0

        for i in grid:
            dic[tuple(i)] += 1

        for i in zip(*grid):
            c += dic[i]
        return c

        