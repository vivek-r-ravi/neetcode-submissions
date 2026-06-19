class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset=set()
        length=0
        L=0
        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L+=1
            hashset.add(s[R])
            length=max(length,R-L+1)
        return length

        

