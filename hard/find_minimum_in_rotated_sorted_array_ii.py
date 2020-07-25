class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        def search(nums: List[int], start, end) -> int:
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return min(nums[0], nums[1])
            
            m = len(nums) // 2
            if nums[m] < start:
                return search(nums[:m+1], start, nums[m])
            elif nums[m] > end:
                return search(nums[m+1:], nums[m], end)
            else:
                return min(
                    search(nums[:m], start, nums[m]),
                    search(nums[m+1:], nums[m], end)
                )
            
        return search(nums, nums[0], nums[-1])
