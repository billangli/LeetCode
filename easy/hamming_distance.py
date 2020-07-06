class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        result = 0
        for _ in range(32):
            if z & 1:
                result += 1
            z >>= 1
        return result
