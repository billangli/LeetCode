class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = [0] * len(arr)
        end = 0
        for i in range(len(arr)):
            if arr[i] % 2 == 0:
                result[i] = end
            else:
                result[i] = 1 + (i - end)
            end = result[i]
        
        return sum(result) % (10**9 + 7)
