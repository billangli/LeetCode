class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += nums[j]
                sums.append(sum_)
                
        sums.sort()
        result = 0
        for i in range(left - 1, right):
            result += sums[i]
        return result % (10 ** 9 + 7)
