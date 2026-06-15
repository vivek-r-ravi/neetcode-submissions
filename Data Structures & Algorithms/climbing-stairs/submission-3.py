# solution 1: brute force recursion
# O(2^n) time and O(n) space due to recursion stack
class SolutionV1:
    def climbStairs(self, n: int) -> int:
        # number of ways to climb to n is equal to sum of the below
        # (i) # ways to climb to (n-1) steps and climb 1 step after
        # (ii) # ways to climb to (n-2) steps and climb 2 step after
        # note: climbing to (n-2) steps and then climbing 1 step 2x not included as this is already counted in (i)
        if n<=2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# solution 2: top-down DP
# O(n) time and space
class Solution:
    def climbStairs(self, n: int) -> int:
        cache={1:1,2:2}
        def memoization(n,cache):
            if n in cache:
                return cache[n]
            cache[n]=memoization(n-1,cache)+memoization(n-2,cache)
            return cache[n]
        return memoization(n,cache)