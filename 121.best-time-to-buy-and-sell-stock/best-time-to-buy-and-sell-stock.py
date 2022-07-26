class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        for p in prices:
            if buy > p:
                buy = p

            elif (p - buy) > max_profit:
                max_profit = p - buy

        return max_profit
