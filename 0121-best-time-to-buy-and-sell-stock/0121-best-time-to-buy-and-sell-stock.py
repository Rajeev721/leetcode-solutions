class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        low, high = 0,1

        while high < len(prices):
            if prices[high] > prices[low]:
                sum = max(sum, prices[high]-prices[low])
            else:
                low = high
            high += 1
        return sum