class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.value = ""
        self.children = []

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            self.children.append(Trie())
            return
        
        for c in self.children:
            if c.value == word[0]:
                c.insert(word[1:])
                return
            
        new = Trie()
        new.value = word[0]
        new.insert(word[1:])
        self.children.append(new)        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        start = word[0] if len(word) > 0 else ""
        for c in self.children:
            if c.value == start:
                if len(word) == 0 or c.search(word[1:]):
                    return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if len(prefix) == 0:
            return True
        
        for c in self.children:
            if c.value == prefix[0]:
                if c.startsWith(prefix[1:]):
                    return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
