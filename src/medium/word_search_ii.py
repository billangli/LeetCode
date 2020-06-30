class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.trie
        for c in word:
            if c not in curr.keys():
                curr[c] = {}
            curr = curr[c]
        curr["."] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.trie
        for c in word: 
            if c not in curr.keys():
                return False
            curr = curr[c]
        return "." in curr.keys()

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.trie
        for c in prefix: 
            if c not in curr.keys():
                return False
            curr = curr[c]
        return True
    
    
class Solution:
    def findWordsGivenStart(self, board: List[List[str]], dict_: dict, x: int, y: int, used: List[tuple]) -> List[str]:
        """Find words from the trie dict_ at the starting point (x, y) that does not repeat on cells in used"""
        suffixes = []
        for c in dict_.keys():
            if board[x][y] == c and (x, y) not in used:
                if "." in dict_[c].keys():
                    suffixes.append(c + ".")
                    
                neighbours = []
                if x + 1 < len(board): neighbours.append((x + 1, y))
                if x - 1 >= 0: neighbours.append((x - 1, y))
                if y + 1 < len(board[0]): neighbours.append((x, y + 1))
                if y - 1 >= 0: neighbours.append((x, y - 1))
                for nx, ny in neighbours:
                    used_copy = [item for item in used]
                    used_copy.append((x, y))
                    c_suffixes = self.findWordsGivenStart(board, dict_[c], nx, ny, used_copy)
                    for cs in c_suffixes:
                        suffixes.append(c + cs)
        return suffixes
        
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Make dict of starting letter to word
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        # Check each cell for the starting letter
        results = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp_results = self.findWordsGivenStart(board, trie.trie, i, j, [])
                for t in temp_results:
                    if t not in results:
                        results.append(t)
                        
        for i in range(len(results)):
            results[i] = results[i][:-1]  # Get rid of the period
        return results
