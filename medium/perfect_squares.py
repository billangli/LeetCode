class Solution:
    def __init__(self):
        self.result = {1: 1}
    
    def numSquares(self, n: int) -> int:
        if n in self.result.keys():
            return self.result[n]
        
        sqrt = math.floor(math.sqrt(n))
        min_ = n
        while 0 < sqrt and min_ * (sqrt ** 2) >= n:
            temp_min = 1 + self.numSquares(n - sqrt ** 2)
            if temp_min < min_:
                min_ = temp_min
            sqrt -= 1
        self.result[n] = min_
        return min_
