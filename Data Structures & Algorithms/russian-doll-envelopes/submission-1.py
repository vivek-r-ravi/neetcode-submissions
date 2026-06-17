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
class Solution:
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

