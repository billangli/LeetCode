class Solution:

    def __init__(self, rects: List[List[int]]):
        self.starts = []
        self.widths = []
        self.areas = []
        for r in rects:
            self.starts.append((r[0], r[1]))
            self.widths.append(r[2] - r[0] + 1)
            self.areas.append((r[2] - r[0] + 1) * (r[3] - r[1] + 1))
        self.total_area = sum(self.areas)

    def pick(self) -> List[int]:
        rand = math.floor(random.random() * self.total_area)
        i = 0
        area_so_far = self.areas[0]
        while i < len(self.areas) - 1 and rand >= area_so_far:
            i += 1
            area_so_far += self.areas[i]
        
        rand_remaining = rand - (area_so_far - self.areas[i])
        width = rand_remaining % self.widths[i]
        height = rand_remaining // self.widths[i]
        
        return [self.starts[i][0] + width, self.starts[i][1] + height]
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
