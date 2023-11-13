class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        left, right = 0, 1

        while right < len(prices):
            # need to check if it makes money
            if(prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right += 1
        

        return maxProfit
