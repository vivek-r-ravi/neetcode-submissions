# brute force
# O(n2) time O(1) space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length=0
        for L in range(n):
            max_f=0
            char_map=dict()
            for R in range(L,n):
                char_map[s[R]]=char_map.get(s[R],0)+1
                max_f=max(max_f,char_map[s[R]])
                if R-L+1-max_f<=k:
                    length=max(length,R-L+1)
                else:
                    break
        return length

'''
# sliding window
# O(n) time O() space
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length = 0
        L = 0
        char_map=dict()
        for R in range(n):
            if s[R] != s[L]:
                L = R
            length = max(length, R - L + 1)
'''