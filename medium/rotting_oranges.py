class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        EMPTY, FRESH, ROTTEN = 0, 1, 2
        M, N = len(grid), len(grid[0])
        num_fresh = 0
        queue = deque()
        seen = [[False] * N for _ in range(M)]
        
        # Count num_fresh and add coordinates with rotten oranges to queue
        for i in range(M):
            for j in range(N):
                if grid[i][j] == FRESH:
                    num_fresh += 1
                elif grid[i][j] == ROTTEN:
                    queue.append((i, j))
                    
        if num_fresh == 0: return 0
                    
        # Items in queue must be an orange
        time = -1
        while num_fresh > 0 and queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                seen[i][j] = True
                
                if grid[i][j] == FRESH:
                    num_fresh -= 1
                    grid[i][j] = 2

                next_coords = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
                for x, y in next_coords:
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != EMPTY and not seen[x][y]:
                        queue.append((x, y))
                        
            time += 1
            
        return -1 if num_fresh else time
