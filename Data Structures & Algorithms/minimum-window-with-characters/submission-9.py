# running match count on dynamic sliding window
# O(n) time O(1) space as counters have at most 52 chars
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        if n < m:
            return ""

        t_count = Counter(t)
        s_count = dict()

        l_min, r_min = 0, float("inf")
        matches = 0
        l = 0
        for r in range(n):
            # expand right
            if s[r] in t_count:
                s_count[s[r]] = s_count.get(s[r], 0) + 1
                if s_count[s[r]] == t_count[s[r]]:
                    matches += 1

            # check valid window and shrink left
            while matches == len(t_count):
                if r - l < r_min - l_min:
                    l_min, r_min = l, r
                if s[l] in t_count:
                    s_count[s[l]] -= 1
                    if s_count[s[l]] + 1 == t_count[s[l]]:
                        matches -= 1
                l += 1

        return s[l_min : r_min + 1] if r_min != float("inf") else ""
