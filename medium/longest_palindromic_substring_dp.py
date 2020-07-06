class Solution:
    def __init__(self):
        pass

    def checkPalindrome(self, s: str) -> str:
        """Check if the given string s is a palindrome"""
        return s[:len(s) // 2] == s[-1:(len(s) - 1) // 2:-1]

    def expandPalindrome(self, p: tuple, s: str):
        longest = p
        while self.checkPalindrome(s[p[0]:p[1]]):
            if not (p[0] > 0 and p[1] < len(s)):
                return p
            longest = p
            p = (p[0] - 1, p[1] + 1)
        return longest
    
    def longestPalindrome(self, s: str) -> str:
        """Find the longest palindrome in string s"""
        if len(s) < 2: return s

        # Loop over palindromes and try to expand them
        longest_palindrome = s[0]
        for i in range(len(s)):
            p = self.expandPalindrome((i, i+ 1), s)
            if p[1] - p[0] > len(longest_palindrome): longest_palindrome = s[p[0]:p[1]]     
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                p = self.expandPalindrome((i, i + 2), s)
                if p[1] - p[0] > len(longest_palindrome): longest_palindrome = s[p[0]:p[1]]        

        return longest_palindrome


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
    print(s.longestPalindrome("cbbd"))
    print(s.longestPalindrome(""))
    print(s.longestPalindrome("a"))
    print(s.longestPalindrome("aa"))
    print(s.longestPalindrome("ab"))
    print(s.longestPalindrome("aaaaajlldllj"))
    