# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        def getHeight(root: TreeNode) -> int:
            if root is None:
                return 0
            return 1 + getHeight(root.left)
        
        left_h = getHeight(root.left)
        right_h = getHeight(root.right)
        if left_h == right_h:
            return (1 << left_h) + self.countNodes(root.right)
        else:
            return (1 << right_h) + self.countNodes(root.left)
