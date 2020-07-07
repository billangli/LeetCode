class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        NO_DIRECTION = -1
        RIGHT = 0
        UP = 1
        LEFT = 2
        DOWN = 3
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        start_i = 0
        start_j = 0
        
        while start_i < m and not grid[start_i][start_j]:
            if start_j == n - 1:
                start_j = 0
                start_i += 1
            else:
                start_j += 1
                
        if start_i == m: 
            return 0
        
        
        def dfs(root_i, root_j, direction):
            visited[root_i][root_j] = True
            sum_ = 0
            if direction != DOWN:
                if root_i + 1 < m:
                    if not visited[root_i + 1][root_j]:
                        sum_ += dfs(root_i + 1, root_j, UP) if grid[root_i + 1][root_j] else 1
                else:
                    sum_ += 1
                
            if direction != LEFT:
                if root_j > 0:
                    if not visited[root_i][root_j - 1]:
                        sum_ += dfs(root_i, root_j - 1, RIGHT) if grid[root_i][root_j - 1] else 1
                else:
                    sum_ += 1
                
            if direction != UP:
                if root_i > 0:
                    if not visited[root_i - 1][root_j]:
                        sum_ += dfs(root_i - 1, root_j, DOWN) if grid[root_i - 1][root_j] else 1
                else:
                    sum_ += 1
                
            if direction != RIGHT:
                if root_j + 1 < n:
                    if not visited[root_i][root_j + 1]:
                        sum_ += dfs(root_i, root_j + 1, LEFT) if grid[root_i][root_j + 1] else 1
                else:
                    sum_ += 1
            return sum_          
        
        
        return dfs(start_i, start_j, NO_DIRECTION)
