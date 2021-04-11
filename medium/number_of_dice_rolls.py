class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d > target or f * d < target: return 0
        
        table = [[0] * (target + 1) for _ in range (d + 1)]
        table[0][0] = 1
            
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                for k in range(1, f + 1):
                    if j - k >= 0:
                        table[i][j] += table[i - 1][j - k]
        
        return table[d][target] % (10 ** 9 + 7)