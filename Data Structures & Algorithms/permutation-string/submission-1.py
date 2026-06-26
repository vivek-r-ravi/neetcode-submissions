# brute force: compare two counters in a fixed sliding window of n_s1 size
# O(n1*n2) time and O(1) space as only 26 letters in dictionary
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)
        if n_s1 > n_s2:
            return False

        count_s1 = Counter(s1)
        count_s2 = dict()
        l = 0
        for r in range(n_s2):
            if r - l + 1 <= n_s1:
                count_s2[s2[r]] = count_s2.get(s2[r], 0) + 1
            if r - l + 1 == n_s1:
                if count_s2 == count_s1:
                    return True
                else:
                    count_s2[s2[l]] -= 1
                    if count_s2[s2[l]] == 0:
                        count_s2.pop(s2[l])
                    l += 1
        return False
