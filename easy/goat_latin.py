class Solution:
    def toGoatLatin(self, S: str) -> str:
        CONSONANTS = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        
        def translate(word: str) -> str:
            if word[0] not in CONSONANTS:
                word = word[1:] + word[0]
            return word + 'ma'
        
        words = S.split()
        result = ""
        for i in range(len(words)):
            result += translate(words[i])
            result += 'a' * (i + 1) + ' '
            
        return result[:-1]
