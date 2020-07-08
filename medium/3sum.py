class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        
        nums.sort()
        
        last_a = None
        for i in range(len(nums) - 2):
            if last_a is None or nums[i] != last_a:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    sum_ = nums[i] + nums[j] + nums[k]
                    if sum_ < 0:
                        j += 1
                    elif sum_ > 0:
                        k -= 1
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            last_a = nums[i]
        return result
