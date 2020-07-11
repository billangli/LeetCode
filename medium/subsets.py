class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerset = [[]]
        for i in range(len(nums)):
            temp = []
            for template in powerset:
                set_ = [x for x in template]
                set_.append(nums[i])
                temp.append(set_)
            powerset.extend(temp)
        return powerset
