# brute force recursion
# O(n^t) exponential time and O(n) space
class SolutionV1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        if amount<0:
            return -1
        min_coins=float('inf')
        for coin in coins:
            curr=self.coinChange(coins,amount-coin)
            if curr>=0:
                min_coins=min(min_coins,curr+1)
        return min_coins if min_coins!=float('inf') else -1

# memoization
# O(n*t) time and O(n) space
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={0:0}
        def memoization(amount):
            if amount<0:
                return -1
            if amount in cache:
                return cache[amount]
            cache[amount]=float('inf')
            for coin in coins:
                curr=memoization(amount-coin)
                if curr>=0:
                    cache[amount]=min(cache[amount],curr+1)
            cache[amount] = cache[amount] if cache[amount]!=float('inf') else -1
            return cache[amount]
        return memoization(amount)