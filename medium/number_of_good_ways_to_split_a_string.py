class Solution:
    def numSplits(self, s: str) -> int:
        i = 0
        last_i = 0
        j = len(s) - 1
        last_j = len(s) - 1
        i_set = set()
        j_set = set()
        
        while i < j and i < len(s) and j >= 0:
            last_i = i
            last_j = j
            while i < len(s) and s[i] in i_set:
                i += 1
            while j >= 0 and s[j] in j_set:
                j -= 1
            if i < len(s):
                i_set.add(s[i])
            if j >= 0:
                j_set.add(s[j])
            
        return min(len(s) - 1, i, last_j) - max(0, j, last_i)
