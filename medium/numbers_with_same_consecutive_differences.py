from typing import List
from collections import defaultdict


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        results = [i for i in range(10)]
        if N == 1:
            return results
        
        table = defaultdict(list)
        for i in range(10):
            if 0 <= i - K <= 9:
                table[i].append(i - K)
            if 0 <= i + K <= 9 and K != 0:
                table[i].append(i + K)
                
        results.remove(0)
        for j in range(N - 1):
            temp_results = []
            for num in results:
                last_digit = num % 10
                for next_digit in table[last_digit]:
                    temp_results.append(num * 10 + next_digit)
            results = temp_results
            
        return results

if __name__ == "__main__":
    s = Solution()
    s.numsSameConsecDiff(3, 7)
