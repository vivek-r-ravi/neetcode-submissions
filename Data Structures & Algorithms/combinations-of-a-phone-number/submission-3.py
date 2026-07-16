# backtracking
# O(n4^n) time O(n) space
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combo, out = [], []

        def dfs(i):
            if i == len(digits):
                out.append("".join(combo))
                return

            for c in digit_map[digits[i]]:
                combo.append(c)
                dfs(i + 1)
                combo.pop()

        if digits:
            dfs(0)
        return out
