class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # table[i] is the number of citations geq i
        table = [0] * (len(citations) + 1)
        
        for c in citations:
            idx = min(len(citations), c)
            table[idx] += 1
            
        for i in range(len(citations), 0, -1):
            if i <= table[i]: 
                return i
            table[i - 1] += table[i]
            
        return 0
