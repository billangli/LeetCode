# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        left_order = self.levelOrderBottom(root.left)
        right_order = self.levelOrderBottom(root.right)
        result = []
        for i in range(-1, -1 - max(len(left_order), len(right_order)), -1):
            row = []
            if len(left_order) + i >= 0:
                row.extend(left_order[i])
            if len(right_order) + i >= 0:
                row.extend(right_order[i])
            result.insert(0, row)
        result.append([root.val])
        return result
