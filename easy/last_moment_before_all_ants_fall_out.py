class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        t_left = max(left) if len(left) else 0
        t_right = n - min(right) if len(right) else 0
        return max(t_left, t_right)
