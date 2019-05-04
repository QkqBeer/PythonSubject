__author__ = "那位先生Beer"
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        sell = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        return sell[-1]

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        prev_sell = 0
        curr_sell = 0
        hold = -prices[0]
        for i in range(1, len(prices)):
            temp = curr_sell
            curr_sell = max(curr_sell, hold + prices[i])
            hold = max(hold, (prev_sell if i >= 2 else 0) - prices[i])
            prev_sell = temp
        return curr_sell