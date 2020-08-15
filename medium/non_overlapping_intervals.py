class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0: return 0
        
        # invervals is reverse sorted list of tuples
        intervals = [tuple(x) for x in intervals]
        array = sorted(intervals, key=lambda x : (x[1], x[0]), reverse=True)
        
        removed_count = 0
        end = array.pop()[1]
        
        while array:
            inter = array.pop()
            if inter[0] < end:
                removed_count += 1
            else:
                end = inter[1]
            
        return removed_count
