class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def placeNum(array: List[int], num: int) -> List[int]:
            """
            Return steps to place num in its place
            Assume A[num:] is already sorted
            """
            if array[num - 1] == num:
                return []
            else:
                idx = array.index(num)
                array[:idx + 1] = array[idx::-1]
                array[:num] = array[num - 1::-1]
                return [idx + 1, num]
            # return [] if A[num - 1] == num else [A.index(num) + 1, num]
            
        
        res = []
        for i in range(len(A), 0, -1):
            res.extend(placeNum(A, i))
        return res
