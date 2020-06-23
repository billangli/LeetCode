from typing import List
import unittest
import collections


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        The idea is to find all sums of pairs and then pair the sums to quads

        freqs: dictionary of frequencies of numbers in nums
        freqs_keys: sorted list of unique numbers in nums
        pairs: dictionary of sum to list of pairs
        pairs_keys: sorted list of pairs sums
        quad: list of four numbers that might be part of result
        """
        if len(nums) < 4:
            return []

        result = []
        nums = sorted(nums)
        for i in range(len(nums) - 3):
            if i != 0 and nums[i - 1] == nums[i]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[len(nums)-3] + nums[len(nums)-2] + nums[len(nums)-1] < target:
                continue

            target_minus_nums_i = target - nums[i]
            for j in range(i + 1, len(nums) - 2):
                if j != i + 1 and nums[j - 1] == nums[j]:
                    continue
                if nums[j] + nums[j+1] + nums[j+2] > target_minus_nums_i:
                    break
                if nums[j] + nums[len(nums)-2] + nums[len(nums)-1] < target_minus_nums_i:
                    continue

                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum_ = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum_ == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])

                    if sum_ <= target:
                        k += 1
                        while nums[k - 1] == nums[k] and k < l:
                            k += 1
                    else:
                        l -= 1
                        while nums[l + 1] == nums[l] and k < l:
                            l -= 1
        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.fn = Solution().fourSum

    def test_example(self):
        self.assertEqual(
            self.fn([1, 0, -1, 0, -2, 2], 0),
            [
                [-1,  0, 0, 1],
                [-2, -1, 1, 2],
                [-2,  0, 0, 2]
            ]
        )

    def test_failure(self):
        self.assertEqual(
            self.fn([-3, -2, -1, 0, 0, 1, 2, 3], 0),
            [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2],
                [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
        )


if __name__ == "__main__":
    # unittest.main()
    # print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    # print(Solution().fourSum([1, 1, 1, 1], 4))
    # print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
    print(Solution().fourSum([0, 0, 0, 0], 0))
