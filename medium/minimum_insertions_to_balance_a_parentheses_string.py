class Solution:
    def minInsertions(self, s: str) -> int:
        i = 0
        result = 0
        open_counter = 0
        
        while i < len(s):
            if s[i] == '(':
                open_counter += 1
                i += 1
            elif i < len(s) - 1 and s[i:i+2] == '))':
                if open_counter > 0:
                    open_counter -= 1
                else:
                    result += 1
                i += 2
            elif s[i] == ')':
                if open_counter > 0:
                    open_counter -= 1
                    result += 1
                else:
                    result += 2
                i += 1
                    
        result += open_counter * 2
        return result
