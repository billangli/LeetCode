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

        nums = sorted(nums)
        freqs = collections.Counter(nums)

        freqs_keys = sorted(freqs.keys())
        pairs = {}
        for i in range(len(freqs_keys)):
            for j in range(i, len(freqs_keys)):
                if freqs_keys[i] == freqs_keys[j] and freqs[freqs_keys[i]] < 2:
                    continue

                pair = [freqs_keys[i], freqs_keys[j]]
                sum_ = freqs_keys[i] + freqs_keys[j]
                if sum_ not in pairs.keys():
                    pairs[sum_] = [pair]
                else:
                    pairs[sum_].append(pair)

        print(pairs)

        # pairs_keys are unique sums of pairs
        result = []
        pairs_keys = sorted(pairs.keys())
        i = 0
        while i < len(pairs_keys):
            j = len(pairs_keys) - 1
            quad_sum = pairs_keys[i] + pairs_keys[j]
            while j >= i and quad_sum >= target:
                quad_sum = pairs_keys[i] + pairs_keys[j]
                if quad_sum == target:
                    k = 0
                    while k < len(pairs[pairs_keys[i]]):
                        l = len(pairs[pairs_keys[j]]) - 1
                        while 0 <= l and (i != j or k <= l):
                            quad = [x for x in pairs[pairs_keys[i]][k]]
                            quad.extend(pairs[pairs_keys[j]][l])
                            quad_freqs = collections.Counter(quad)
                            success = True
                            for key in quad_freqs.keys():
                                if quad_freqs[key] > freqs[key]:
                                    success = False
                            if success:
                                quad = sorted(quad)
                                def list_equals(x, y): return collections.Counter(
                                    x) == collections.Counter(y)
                                for r in result:
                                    if list_equals(quad, r):
                                        success = False
                                if success:
                                    result.append(sorted(quad))
                            l -= 1
                        k += 1
                j -= 1
            i += 1
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
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
