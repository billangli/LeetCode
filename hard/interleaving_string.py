class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        if n + m != len(s3): return False
        if n == 0: return s2 == s3
        if m == 0: return s1 == s3
        
        s1_next = {0}
        for k in range(len(s3)):
            print(k, s1_next)
            if len(s1_next) == 0: return False
            
            temp_s1_next = set()
            for i in s1_next:
                j = k - i
                if i < n and s1[i] == s3[k]:
                    temp_s1_next.add(min(i + 1, n))
                if j < m and s2[j] == s3[k]:
                    temp_s1_next.add(i)
                    
            s1_next = temp_s1_next
            
        return True
