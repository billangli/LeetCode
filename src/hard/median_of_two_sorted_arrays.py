import unittest
from typing import List


class Solution():
    def median(self, nums: List[int]) -> float:
        m_index = (len(nums) - 1) // 2
        return (nums[m_index] + nums[m_index + 1]) / 2 if len(nums) % 2 == 0 else nums[m_index]

    def findMediansByIfs(self, nums1: List[int], nums2: List[int]) -> float:
        """Assume that 0 <= len(nums1), len(nums2) <= 2"""
        print(nums1, nums2)
        if len(nums1) == 1:
            if len(nums2) == 1:
                return (nums1[0] + nums2[0]) / 2
            else:
                if nums1[0] <= nums2[0]:
                    return nums2[0]
                return nums2[1] if nums1[0] >= nums2[1] else nums1[0]
        else:
            if len(nums2) == 1:
                if nums2[0] <= nums1[0]:
                    return nums1[0]
                return nums1[1] if nums2[0] >= nums1[1] else nums2[0]
            else:
                return (max(nums1[0], nums2[0]) + min(nums1[1], nums2[1])) / 2

    def findMediansBruteForce(self, nums1: List[int], nums2: List[int]) -> float:
        """Assume that 2 < len(nums1), len(nums2) <= 4"""
        print("findMediansBruteForce", nums1, nums2)
        even = (len(nums1) + len(nums2)) % 2 == 0
        iters = len(nums1) + len(nums2) - (len(nums1) + len(nums2) - 1) // 2
        i = 0
        j = 0
        prev = nums1[0]
        curr = nums1[0]
        while i + j < iters and i < len(nums1) and j < len(nums2):
            prev = curr
            if nums1[i] <= nums2[j]:
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if i + j == iters:
            return (prev + curr) / 2 if even else curr

        remaining = nums1 if j == len(nums2) else nums2
        finished_idx = j if j == len(nums2) else i
        if even:
            if iters - i - j == 1:
                return (curr + remaining[iters - finished_idx - 1]) / 2
            else:
                return (remaining[iters - finished_idx - 2] + remaining[iters - finished_idx - 1]) / 2
        else:
            return remaining[iters - finished_idx - 1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print(nums1, nums2)
        if len(nums1) == 0:
            m_index = (len(nums2) - 1) // 2
            return (nums2[m_index] + nums2[m_index+1]) / 2 if len(nums2) % 2 == 0 else nums2[m_index]
        if len(nums2) == 0:
            m_index = (len(nums1) - 1) // 2
            return (nums1[m_index] + nums1[m_index+1]) / 2 if len(nums1) % 2 == 0 else nums1[m_index]
        if len(nums1) <= 2 and len(nums2) <= 2:
            return self.findMediansByIfs(nums1, nums2)
        elif len(nums1) <= 4 and len(nums2) <= 4:
            return self.findMediansBruteForce(nums1, nums2)

        longer = nums1 if len(nums1) > len(nums2) else nums2
        shorter = nums2 if len(nums1) > len(nums2) else nums1
        ml = self.median(longer)
        ms = self.median(shorter)
        if ml == ms:
            return ms

        # Case 1: ml < ms, case 2: ml > ms
        # In each list, remove numbers from the side that is more extreme than
        # the median, then remove numbers from the less extreme side in the long
        # list to make sure that the same numbers of numbers are removed from
        # both lists
        case1 = ml < ms
        # The number of items removed from each list / 2
        s_removed = max((len(shorter) - 1) // 2, 0)
        l_removed = max(
            min(
                (len(longer) - 1) // 2 - 1,
                (len(longer) - len(shorter) - 1) // 2
            ),
            s_removed
        )

        s_start = 0 if case1 else s_removed
        s_end = len(shorter) - s_removed if case1 else len(shorter)
        l_start = l_removed if case1 else max(l_removed - s_removed, 0)
        l_end = len(longer) - l_removed + s_removed if case1 \
            else len(longer) - l_removed

        if l_end - l_start <= 2 and s_end - s_start <= 2:
            return self.findMediansBruteForce(longer[l_start:l_end], shorter[s_start:s_end])
        else:
            return self.findMedianSortedArrays(longer[l_start:l_end], shorter[s_start:s_end])


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        self.fn = self.solution.findMedianSortedArrays
        self.bf = self.solution.findMediansBruteForce

    def test_brute_force(self):
        self.assertEqual(self.bf([1, 3], [2]), 2)
        self.assertEqual(self.bf([1, 2], [3, 4]), 2.5)
        self.assertEqual(self.bf([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], [3]), 5.5)
        self.assertEqual(
            self.bf([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], [3, 3, 3]), 4.5)

    def test_empty(self):
        self.assertEqual(self.fn([], [2]), 2)
        self.assertEqual(self.fn([], [2, 3]), 2.5)
        self.assertEqual(self.fn([], [2, 3, 6, 7]), 4.5)
        self.assertEqual(self.fn([2, 3, 6, 7], []), 4.5)

    def test_simple(self):
        self.assertEqual(self.fn([1, 3], [2]), 2)

    def test_example(self):
        self.assertEqual(self.fn([1, 2], [3, 4]), 2.5)

    def test_insert(self):
        self.assertEqual(self.fn([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], [3]), 5.5)

    def test_insert2(self):
        self.assertEqual(
            self.fn([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], [3, 3, 3]), 4.5)

    def test_insert3(self):
        self.assertEqual(
            self.fn([1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], [7, 8, 9]), 7)

    def test_insert4(self):
        self.assertEqual(self.fn([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]), 5.5)


if __name__ == "__main__":
    unittest.main()
