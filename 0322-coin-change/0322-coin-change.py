class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hashmap = [float('inf')] * (amount + 1)
        hashmap[0] = 0
        def minchange(amount, coins):
            for coin in coins:
                for i in range(coin, amount + 1):
                    sub = i - coin
                    if sub <0:
                        continue
                    hashmap[i] = min(hashmap[i], hashmap[sub] +1)
            return -1 if hashmap[amount] == float('inf') else hashmap[amount]
        return minchange(amount, coins)
