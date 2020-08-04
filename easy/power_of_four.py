class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num & 0xaaaaaaaa == 0 and num & 0x55555555 != 0 and num & (num - 1) == 0
