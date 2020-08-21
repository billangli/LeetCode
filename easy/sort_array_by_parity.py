class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        result = [0] * len(A)
        i, j = 0, len(A) - 1
        for num in A:
            if num % 2 == 0:
                result[i] = num
                i += 1
            else:
                result[j] = num
                j -= 1
        return result
