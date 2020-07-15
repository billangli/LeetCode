class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        if len(words) == 0:
            return ""
        result = ""
        for i in range(len(words) - 1, -1, -1):
            result += words[i] + " "
        return result[:-1]
