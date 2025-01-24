class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        min_price = float('inf')
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                current_profit = price - min_price
                if current_profit > m:
                    m = current_profit

        return m