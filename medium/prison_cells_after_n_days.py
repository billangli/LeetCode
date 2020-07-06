class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        if N == 0:
            return cells
        
        bit_cells = 0
        for i in range(len(cells)):
            bit_cells += cells[- i - 1] << i
            
        history = []
        used = {}
            
        for i in range(N):
            bit_cells = ~((bit_cells >> 1) ^ (bit_cells << 1))
            bit_cells &= 0b01111110
            
            if used.get(bit_cells):
                # Find the result using cycles
                iters_left = N - i - 1
                cycle_start_idx = history.index(bit_cells)
                cycle_length = len(history) - cycle_start_idx
                bit_cells = history[cycle_start_idx + iters_left % cycle_length]
                break
            else:
                used[bit_cells] = True
                history.append(bit_cells)
            
        result = []
        for i in range(len(cells) - 1, -1, -1):
            result.append((bit_cells >> i) & 1)
        return result
