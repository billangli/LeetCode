class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:        
        def search(board: List[List[str]], word: str, x: int, y: int, used: list) -> bool:
            if (x, y) not in used and board[x][y] == word[0]:
                if len(word) == 1:
                    return True
                
                used.add((x, y))
                coords = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
                for c in coords:
                    if 0 <= c[0] < len(board) and 0 <= c[1] < len(board[0]):
                        if search(board, word[1:], c[0], c[1], used):
                            return True
                used.remove((x, y))
            return False
            
            
        used = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if search(board, word, i, j, used):
                    return True
        return False
