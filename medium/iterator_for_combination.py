class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # These values will be for the next word
        self.chars = characters
        self.len = combinationLength
        self.next_exists = combinationLength <= len(characters)
        self.pointers = [i for i in range(combinationLength)]

    def next(self) -> str:
        result = ""
        for ptr in self.pointers:
            result += self.chars[ptr]
            
        # Update pointers and don't bother if next doesn't exist
        if self.pointers[0] < len(self.chars) - self.len:
            i = self.len - 1
            final_pos = len(self.chars) - 1
            while self.pointers[i] == final_pos:
                i -= 1
                final_pos -= 1
                
            self.pointers[i] += 1
            for j in range(i + 1, self.len):
                self.pointers[j] = self.pointers[i] + j - i
        else:
            self.next_exists = False
        
        return result

    def hasNext(self) -> bool:
        return self.next_exists


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
