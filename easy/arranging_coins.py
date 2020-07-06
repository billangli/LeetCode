class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = math.floor(math.sqrt(2 * n))
        return i if i * (i + 1) / 2 <= n else i - 1
