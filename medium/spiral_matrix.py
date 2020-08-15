class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        if n == 0: return []
        
        result = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1 , 0)]
        curr_dir = 0
        x, y = 0, 0
        
        for _ in range(m * n):
            result.append(matrix[x][y])
            matrix[x][y] = '$'
            next_x, next_y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]
            if 0 <= next_x < m and 0 <= next_y < n and matrix[next_x][next_y] != '$':
                x, y = next_x, next_y
            else:
                curr_dir = (curr_dir + 1) % len(dirs)
                x, y = x + dirs[curr_dir][0], y + dirs[curr_dir][1]
                
        return result
