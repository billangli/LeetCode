class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(string, num_unclosed, num_open_remaining):
            if len(string) == 2 * n:
                return [string]
            result = []
            if num_unclosed > 0:
                result.extend(dfs(string + ")", num_unclosed - 1, num_open_remaining))
            if num_open_remaining > 0:
                result.extend(dfs(string + "(", num_unclosed + 1, num_open_remaining - 1))
            return result
                
        return dfs("", 0, n)
