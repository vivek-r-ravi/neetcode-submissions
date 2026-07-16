class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combo, out = [], []

        def dfs(open, close):
            if open == close == n:
                out.append("".join(combo))
                return

            # include open
            if open < n:
                combo.append("(")
                dfs(open + 1, close)
                combo.pop()

            # include close
            if open > close:
                combo.append(")")
                dfs(open, close + 1)
                combo.pop()

        dfs(0, 0)
        return out
