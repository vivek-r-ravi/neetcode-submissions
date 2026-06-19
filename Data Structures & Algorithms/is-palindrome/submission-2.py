# brute force
# O(n) time and space
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr[::-1]==newStr

# two pointers
# O(n) time O(1) space