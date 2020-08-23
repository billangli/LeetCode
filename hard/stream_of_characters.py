class Trie:
    def __init__(self):
        self.root = {}
        self.currs = [self.root]
        
    def insert(self, word: str) -> None:
        word += '$'
        node = self.root
        while len(word) > 0 and word[0] in node:
            node = node[word[0]]
            word = word[1:]
        if len(word) == 0: return
        
        for letter in word:
            node[letter] = {}
            node = node[letter]
            
    def query(self, letter: str) -> bool:
        temp = [self.root]
        result = False
        for curr in self.currs:
            if letter in curr:
                curr = curr[letter]
                if '$' in curr:
                    result = True
                temp.append(curr)
        self.currs = temp
        return result
                   
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)        
        print(self.trie.root)

    def query(self, letter: str) -> bool:
        return self.trie.query(letter)
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
