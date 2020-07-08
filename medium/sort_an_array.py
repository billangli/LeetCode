class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(nums: List[int], lo: int, hi: int) -> List[int]:
            if lo < hi - 1:
                p = partition(nums, lo, hi)
                quicksort(nums, lo, p)
                quicksort(nums, p + 1, hi)
            return nums

        def swap(nums: List[int], i: int, j: int) -> None:
            """Swap items i and j in the list nums"""
            nums[i], nums[j] = nums[j], nums[i]

        def partition(nums: List[int], lo: int, hi: int) -> int:
            """Return index j in [lo, hi) where nums[lo:j] are all smaller
            than nums[j] and nums[j + 1:hi] are all larger than nums[j]"""
            i = lo
            pivot = nums[hi - 1]
            for j in range(lo, hi - 1):
                if nums[j] < pivot:
                    swap(nums, i, j)
                    i += 1
            swap(nums, i, hi - 1)
            return i

        def mergesort(nums: List[int]) -> List[int]:
            if len(nums) < 2:
                return nums
            elif len(nums) == 2:
                return [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]
            else:
                p = len(nums) // 2
                n1, n2 = mergesort(nums[:p]), mergesort(nums[p:])
                result = []
                i1, i2 = 0, 0
                while i1 < len(n1) and i2 < len(n2):
                    if n1[i1] < n2[i2]:
                        result.append(n1[i1])
                        i1 += 1
                    else:
                        result.append(n2[i2])
                        i2 += 1
                if i1 < len(n1):
                    result.extend(n1[i1:])
                elif i2 < len(n2):
                    result.extend(n2[i2:])
            return result


        # quicksort(nums, 0, len(nums))
        # return nums
        return mergesort(nums)
