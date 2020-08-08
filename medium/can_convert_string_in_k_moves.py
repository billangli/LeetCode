class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        shifts = defaultdict(int)
        for i in range(26):
            shifts[i] = (k - i - 1) // 26 + 1
            
        for i in range(len(s)):
            diff = (ord(t[i]) - ord(s[i]) + 26) % 26
            if diff != 0:
                if shifts[diff - 1] == 0:
                    return False
                else:
                    shifts[diff - 1] -= 1
                    
        return True
