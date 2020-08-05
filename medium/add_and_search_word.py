class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        # Find split node
        word += '0'
        curr = self.trie
        i = 0
        while i < len(word) and word[i] in curr:
            curr = curr[word[i]]
            i += 1
        
        # Add the rest of the word
        while i < len(word):
            curr[word[i]] = {}
            curr = curr[word[i]]
            i += 1
            
    def _search(self, word: str, root: dict) -> bool:
        if len(word) == 1:
            return '0' in root
        
        if word[0] == '.':
            for key in root.keys():
                if self._search(word[1:], root[key]):
                    return True
        else:
            if word[0] in root:
                return self._search(word[1:], root[word[0]])
            
        return False
        
    def search(self, word: str, root: dict = None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        word += '0'
        return self._search(word, self.trie)
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
