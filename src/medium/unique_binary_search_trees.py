class Solution:
    def __init__(self):
        self.answers = {0: 1, 1: 1}
    
    def numTrees(self, n: int) -> int:
        if n in self.answers.keys():
            return self.answers[n]
        
        result = 0
        for i in range(n):
            result += self.numTrees(i) * self.numTrees(n - 1 - i)
        self.answers[n] = result
        return result
