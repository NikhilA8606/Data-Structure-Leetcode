121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, p: List[int]) -> int:
        min_buy = p[0]
        profit = 0
        for i in p[1:]:
            if i < min_buy:
                min_buy = i
            else:
                profit = max(profit, i - min_buy)
        return profit
        