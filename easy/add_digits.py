class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        result = num % 9
        return 9 if result == 0 else result
