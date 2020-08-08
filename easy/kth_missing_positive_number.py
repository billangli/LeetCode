class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        k -= arr[0] - 1
        
        i = 0
        while i < len(arr) - 1:
            diff = arr[i + 1] - arr[i]
            if diff != 1:
                if diff > k:
                    return arr[i] + k
                else:
                    k -= diff - 1
            i += 1
        return arr[-1] + k
