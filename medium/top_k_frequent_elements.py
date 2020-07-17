class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = {}
        for num in nums:
            if num in occurences.keys():
                occurences[num] += 1
            else:
                occurences[num] = 1
        
        result = list(occurences.keys())
        result = sorted(result, reverse=True, key=lambda x: occurences[x])
        return result[:k]
