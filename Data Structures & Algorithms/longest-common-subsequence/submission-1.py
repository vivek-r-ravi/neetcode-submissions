# brute force recursion
# exponential O(2^m+n) time and O(m+n) space
class SolutionV1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        # dfs(x,y) is the length of LCS with first x and y indicies of text1 and text2
        def dfs(x,y):
            if x<0 or y<0:
                return 0
            if text1[x]==text2[y]:
                return 1+dfs(x-1,y-1)
            else:
                return max(dfs(x,y-1),dfs(x-1,y))
        return dfs(m-1,n-1)

# memoization
# O(mn) time and O(m+n) space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m=len(text1)
        n=len(text2)
        cache=[[0]*n for i in range(m)]
        # dfs(x,y) is the length of LCS with first x and y indicies of text1 and text2
        def dfs(x,y):
            if x<0 or y<0:
                return 0
            if cache[x][y]!=0:
                return cache[x][y]
            if text1[x]==text2[y]:
                cache[x][y]=1+dfs(x-1,y-1)
            else:
                cache[x][y]=max(dfs(x,y-1),dfs(x-1,y))
            return cache[x][y]
        return dfs(m-1,n-1)