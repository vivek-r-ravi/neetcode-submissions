# brute force
# O(n2) time O(1) space as dict can have at most 26 keys
class SolutionV1:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length = 0
        for L in range(n):
            max_f = 0
            char_map = dict()
            for R in range(L, n):
                char_map[s[R]] = char_map.get(s[R], 0) + 1
                max_f = max(max_f, char_map[s[R]])
                if R - L + 1 - max_f <= k:
                    length = max(length, R - L + 1)
                else:
                    break
        return length


# sliding window
# O(n) time O(1) space as dict can have at most 26 keys
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        length = 0
        L = 0
        max_f = 0
        char_map = dict()
        for R in range(n):
            char_map[s[R]] = char_map.get(s[R], 0) + 1
            max_f = max(max_f, char_map[s[R]])
            while R - L + 1 - max_f > k:
                char_map[s[L]] -= 1
                L += 1
            length = max(length, R - L + 1)
        return length
