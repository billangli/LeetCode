class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        min_ = target[0]
        for i in range(1, len(target)):
            if target[i] < min_:
                min_ = target[i]
            elif target[i] > min_:
                result += target[i] - min_
                min_ = target[i]
        return result
