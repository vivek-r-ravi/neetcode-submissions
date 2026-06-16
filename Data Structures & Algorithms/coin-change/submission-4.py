# brute force recursion
# O(n^t) exponential time and O(n) space
class SolutionV1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        min_coins = float("inf")
        for coin in coins:
            curr = self.coinChange(coins, amount - coin)
            if curr >= 0:
                min_coins = min(min_coins, curr + 1)
        return min_coins if min_coins != float("inf") else -1


# memoization
# O(n*t) time and O(t) space
class SolutionV2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0: 0}

        def memoization(amount):
            if amount < 0:
                return -1
            if amount in cache:
                return cache[amount]
            cache[amount] = float("inf")
            for coin in coins:
                curr = memoization(amount - coin)
                if curr >= 0:
                    cache[amount] = min(cache[amount], curr + 1)
            cache[amount] = cache[amount] if cache[amount] != float("inf") else -1
            return cache[amount]

        return memoization(amount)


# tabulation
# O(n*t) time and O(t) space
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for amt in range(amount + 1):
                if amt >= coin:
                    dp[amt] = min(dp[amt], 1 + dp[amt - coin])
        return dp[amount] if dp[amount] != float("inf") else -1


# BFS with each vertex being amount and edge as using 1 coin
# find shortest path length from 0 to amount
# O(n*t) time and O(t) space
class SolutionV4:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([0])
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    nxt = cur + coin
                    if nxt == amount:
                        return res
                    if nxt > amount or seen[nxt]:
                        continue
                    seen[nxt] = True
                    q.append(nxt)

        return -1
