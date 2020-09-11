class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        dp_pos, dp_neg = [0] * (len(nums) + 1), [0] * (len(nums) + 1)
        for i in range(len(nums)):
            dp_pos[i] = max(
                0,
                nums[i],
                dp_pos[i - 1] * nums[i],
                dp_neg[i - 1] * nums[i]
            )
            dp_neg[i] = min(
                0,
                nums[i],
                dp_pos[i - 1] * nums[i],
                dp_neg[i - 1] * nums[i]
            )
        return max(dp_pos)
