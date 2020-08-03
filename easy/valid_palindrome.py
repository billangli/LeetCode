class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not (s[i].isalpha() or s[i].isnumeric()):
                i += 1
            while i < j and not (s[j].isalpha() or s[j].isnumeric()):
                j -= 1
            if i < j and s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
