# compare two hash map counter in a fixed sliding window of n_s1 size
# O(n) time and O(1) space as only 26 letters in dictionary
# n is size of s2, counter comparison is O(26)
class SolutionV1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)

        if n_s1 > n_s2:
            return False

        count_s1 = Counter(s1)
        count_s2 = dict()
        l = 0
        for r in range(n_s2):
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


# canonical solution: maintain match count for sliding window
# O(n) time and O(1) space as only 26 letters in dictionary
# n is size of s2, counter comparison is O(26)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n_s1 = len(s1)
        n_s2 = len(s2)

        if n_s1 > n_s2:
            return False

        count_s1 = [0] * 26
        for s in s1:
            count_s1[ord(s) - ord("a")] += 1
        count_s2 = [0] * 26

        matches = 0
        for c_s1, c_s2 in zip(count_s1, count_s2):
            matches += 1 if c_s1 == c_s2 else 0

        l = 0
        for r in range(n_s2):
            
            idx = ord(s2[r]) - ord("a")
            count_s2[idx] += 1
            if count_s2[idx] == count_s1[idx]:
                matches += 1
            elif count_s2[idx]-1 == count_s1[idx]:
                matches -= 1

            if r - l + 1 == n_s1:
                if matches == 26:
                    return True
                else:
                    idx = ord(s2[l]) - ord("a")
                    count_s2[idx] -= 1
                    if count_s2[idx] == count_s1[idx]:
                        matches += 1
                    elif count_s2[idx] + 1 == count_s1[idx]:
                        matches -= 1
                    l += 1

        return False
