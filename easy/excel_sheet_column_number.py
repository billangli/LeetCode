class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            result += (26 ** i) * (ord(s[len(s) - 1 - i]) - 64)
        return result
