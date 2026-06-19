class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length=0
        for L in range(n):
            rem=k
            R=L
            while R<n and L>=0:
                if s[L]!=s[R]:
                    if rem>0:
                        rem-=1
                    else:
                        break
                length=max(length,R-L+1)
                if R==n-1:
                    L-=1
                else:
                    R+=1
            '''
            for R in range(L,n):
                if s[L]!=s[R]:
                    if rem>0:
                        rem-=1
                    else:
                        break
                length=max(length,R-L+1)
            while R==n-1 and L>=0:
                if s[L]!=s[R]:
                    if rem>0:
                        rem-=1
                    else:
                        break
                length=max(length,R-L+1)
                L-=1
            '''
        return length

'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length = 0
        L = 0
        for R in range(n):
            if s[R] != s[L]:
                L = R
            length = max(length, R - L + 1)
'''