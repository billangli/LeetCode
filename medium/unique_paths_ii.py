class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        num_paths = [[0] * n for _ in range(m)]
        num_paths[m - 1][n - 1] = 1
        
        for sum_ in range(m + n - 3, -1, -1):
            for i in range(max(sum_ - n + 1, 0), min(sum_ + 1, m)):
                j = sum_ - i
                if i + 1 < m and not obstacleGrid[i + 1][j]:
                    num_paths[i][j] += num_paths[i + 1][j]
                if j + 1 < n and not obstacleGrid[i][j + 1]:
                    num_paths[i][j] += num_paths[i][j + 1]
                    
        return num_paths[0][0]
