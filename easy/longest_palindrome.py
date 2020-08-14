class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd = set()
        for char in s:
            if char not in odd:
                odd.add(char)
            else:
                odd.remove(char)
        return len(s) - len(odd) + 1 if len(odd) > 0 else len(s)
