class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        def char_to_int(char: str) -> int:
            """Convert lower-case character to int starting at 'a' = 0"""
            return ord(char) - 97
        
        def int_to_char(num: int) -> str:
            """Convert number to lower-case letter starting at 0 = 'a'"""
            return chr(num + 97)
        
        n = len(A)
        table = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for j in range(len(A[i])):
                table[i][char_to_int(A[i][j])] += 1
        
        result = []
        for j in range(26):
            occurence = min([x[j] for x in table])
            result.extend([int_to_char(j)] * occurence)
        
        return result
