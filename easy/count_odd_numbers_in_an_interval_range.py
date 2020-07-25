class Solution:
    def countOdds(self, low: int, high: int) -> int:
        result = high - low + 1
        if result % 2 == 0:
            return result // 2
        else:
            if low % 2 == 1:
                return result // 2 + 1
            else:
                return result // 2
