# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = 0
        if root is None:
            return result
        if root.left:
            if root.left.left is None and root.left.right is None:
                result += root.left.val
            result += self.sumOfLeftLeaves(root.left)
        if root.right:
            result += self.sumOfLeftLeaves(root.right)
        return result
