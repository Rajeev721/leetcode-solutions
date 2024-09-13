class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low , high = 0, 1
        max_val = 0

        while high < len(prices):
            if prices[low] < prices[high]:
                p = prices[high] - prices[low]

                max_val = max(max_val, p)
            else:
                low = high
            high += 1
        return max_val
