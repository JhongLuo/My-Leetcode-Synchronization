class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        res = 0
        for i in range(1, len(prices)):
            min_price = min(prices[i], min_price)
            res = max(prices[i] - min_price, res)
        return res
            
            