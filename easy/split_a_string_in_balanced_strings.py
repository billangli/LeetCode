class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        l_count = 0
        r_count = 0
        
        for letter in s:
            if letter == 'L':
                l_count += 1
            else:
                r_count += 1
                
            if l_count == r_count and l_count != 0:
                result += 1
                l_count = 0
                r_count = 0
                
        return result
