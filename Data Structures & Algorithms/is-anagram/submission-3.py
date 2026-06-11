# naive solution: sorting both strings and compare. O(mlogm + nlogn) time.

# canonical solution: compare the two counter dictionaries
# O(m+n) time and O(1) space as there are only 26 alphabets
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        return Counter(s)==Counter(t)

        