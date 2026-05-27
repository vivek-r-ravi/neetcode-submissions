class Solution:
    def isValid(self, s: str) -> bool:
        curr = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for p in s:
            if p in pairs.values():
                curr.append(p)
            else:
                if curr and pairs[p]==curr[-1]:
                    curr.pop()
                else:
                    return False
        return len(curr)==0