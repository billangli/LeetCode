class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1] * n for _ in range(m)]
        grid[m - 1][n - 1] = 1
        for s in range(m + n - 3, -1, -1):
            for i in range(max(s - (n - 1), 0), min(s + 1, m)):
                j = s - i
                sum_ = 0
                if i + 1 < m:
                    sum_ += grid[i + 1][j]
                if j + 1 < n:
                    sum_ += grid[i][j + 1]
                grid[i][j] = sum_
        return grid[0][0]
