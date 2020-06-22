class Solution:
    def checkPalindrome(self, s: str) -> str:
        """Check if the given string s is a palindrome"""
        # return s[:len(s) // 2] == s[(len(s) + 1) // 2::-1]
        return s == s[::-1]
    
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        for p_len in range(len(s), 0, -1):
            for start in range(0, len(s) - p_len + 1):
                if self.checkPalindrome(s[start:start+p_len]):
                    return s[start:start+p_len]