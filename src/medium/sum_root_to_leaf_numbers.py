# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def getNumbers(self, root: TreeNode) -> int:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        val_str = str(root.val)
        nums = self.getNumbers(root.left)
        nums.extend(self.getNumbers(root.right))
        for i in range(len(nums)):
            nums[i] = val_str + nums[i]
        return nums
            
    
    def sumNumbers(self, root: TreeNode) -> int:
        sum_ = 0
        for n in self.getNumbers(root):
            sum_ += int(n)
        return sum_
