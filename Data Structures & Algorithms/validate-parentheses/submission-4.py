class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        pairs = {")": "(", "]": "[", "}": "{"}
        for p in s:
            if p in pairs:
                if curr and pairs[p] == curr[-1]:
                    curr.pop()
                else:
                    return False
            else:
                curr.append(p)
        return len(curr) == 0
