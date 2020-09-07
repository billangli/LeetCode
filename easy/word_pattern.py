class Solution:
    def wordPattern(self, pattern: str, sentence: str) -> bool:
        words = sentence.split()
        if len(pattern) != len(words): return False
        
        lookup = {}
        used = set()
        for i in range(len(pattern)):
            if pattern[i] in lookup and lookup[pattern[i]] != words[i]:
                return False
            
            if pattern[i] not in lookup and words[i] in used:
                return False
            
            lookup[pattern[i]] = words[i]
            used.add(words[i])
                
        return True
