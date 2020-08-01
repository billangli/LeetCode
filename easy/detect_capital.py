class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[a-z]+|[A-Z]+|[A-Z][a-z]+", word)
