class Solution:
    def nthRindex(self, string: str, n: int) -> int:
        end = len(string)
        while n >= 0:
            idx = string.rindex("(", 0, end)
            end = idx
            n -= 1
        return idx
    
    def swap(self, string: str, i: int, j: int) -> str:
        """Swap chars in indices i and j in string, i < j"""
        return string[:i] + string[j] + string[i + 1:j] + string[i] + string[j + 1:]
    
    def well_formed(self, string: str) -> bool:
        """Check if the string is well formed"""
        count = 0
        for i in range(len(string)):
            count += 1 if string[i] == "(" else -1
            if count < 0:
                return False
        return True
    
    def generateParenthesis(self, n: int) -> List[str]:
        queue = ["(" * n + ")" * n]
        results = ["(" * n + ")" * n]
        for i in range(n - 1):
            temp = []
            while len(queue):
                string = queue.pop()
                # Move ith ( in reverse order to the right until not possible 
                open_idx = self.nthRindex(string, i)
                swap_idx = open_idx + 1
                new_string = self.swap(string, open_idx, swap_idx)
                while swap_idx < len(string) - 1 and self.well_formed(new_string):
                    if new_string not in results:
                        results.append(new_string)
                        temp.append(new_string)
                    swap_idx += 1
                    new_string = self.swap(string, open_idx, swap_idx)
            queue = temp
        return results
