# brute force recursion
class SolutionV1:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort()
        # dfs(x) is max # of envelopes at end of x index in envelopes
        def dfs(x):
            best = 1
            w_x, h_x = envelopes[x]
            for i in range(x):
                w, h = envelopes[i]
                if w < w_x and h < h_x:
                    best = max(best,dfs(i)+1)
            return best
        return max(dfs(i) for i in range(n))

# memoization
# O(n2) time, O(n) space
class SolutionV2:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort()
        cache={0:1}
        def dfs(x):
            if x in cache:
                return cache[x]
            best=1
            w_x, h_x = envelopes[x]
            for j in range(x):    
                w, h = envelopes[j]
                if w < w_x and h < h_x:
                    best=max(best,1+dfs(j))
            cache[x]=best
            return cache[x]
        return max(dfs(i) for i in range(n))

# tabulation
# O(n2) time, O(n) space
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        n = len(envelopes)
        envelopes.sort()
        # state: dp[i] is max # of envelopes at end of x index in envelopes
        dp=[1]*n
        dp_best=1
        for i in range(n):
            w_x, h_x = envelopes[i]
            for j in range(i):
                w, h = envelopes[j]
                if w < w_x and h < h_x:
                    dp[i]=max(dp[i],1+dp[j])
            dp_best=max(dp_best,dp[i])
        return dp_best

