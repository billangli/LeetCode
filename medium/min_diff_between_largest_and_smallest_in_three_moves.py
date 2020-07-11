class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        
        highest4 = sorted(nums[:4])
        lowest4 = sorted(nums[:4])
        for i in range(4, len(nums)):
            if nums[i] > highest4[0]:
                highest4[0] = nums[i]
                highest4.sort()
            if nums[i] < lowest4[3]:
                lowest4[3] = nums[i]
                lowest4.sort()
            
        return min([highest4[i] - lowest4[i] for i in range(4)])
