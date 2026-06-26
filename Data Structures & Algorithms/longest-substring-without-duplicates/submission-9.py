# canonical solution 1: sliding window with set
# O(n) time O(n) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in hashset:
                hashset.remove(s[L])
                L += 1
            hashset.add(s[R])
            length = max(length, R - L + 1)
        return length


# canonical solution 2: sliding window with dictionary
# O(n) time O(n) space
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = dict()
        length = 0
        L = 0
        for R in range(len(s)):
            if s[R] in hashmap:
                L = max(L, hashmap[s[R]] + 1)
            hashmap[s[R]] = R
            length = max(length, R - L + 1)
        return length
