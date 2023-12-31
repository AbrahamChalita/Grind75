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

"""

Initialize maxProfit and two pointers. Use while, for each pair check it profitable and store the max. If not profit move left = right. Either case move right one.

"""
