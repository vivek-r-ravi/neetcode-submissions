from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict=Counter(s)
        t_dict=Counter(t)
        for i in s_dict:
            if s_dict[i]!=t_dict[i]:
                return False
        for i in t_dict:
            if s_dict[i]!=t_dict[i]:
                return False
        return True

        