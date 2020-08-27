class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        tree = [tuple(x) for x in intervals]
        length = len(intervals)
        
        table = {}
        for i in range(length):
            table[tree[i]] = i
            
        tree = sorted(tree, key=lambda x: (x[0], x[1]))
        
        def binarySearch(array, start, end, key):
            """
            Return the index of the interval in array[start:end] such that interval[0] > key
            """
            if start >= end: return -1
            if start + 1 == end: return start if array[start][0] >= key else -1
            
            mid = start + (end - start) // 2
            if array[mid][0] < key:
                return binarySearch(array, mid + 1, end, key)
            else:
                res = binarySearch(array, start, mid, key)
                return mid if res == -1 else res
            
        
        result = []
        for inter in intervals:
            i = binarySearch(tree, 0, length, inter[1])
            result.append(-1 if i == -1 else table[tree[i]])
        return result
