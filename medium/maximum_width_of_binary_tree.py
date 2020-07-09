# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:        
        def dfs(root: TreeNode, num: int, level: int) -> int:
            if root is None:
                return 0
            
            root.val = num
            if len(leftmost) < level:
                leftmost.append(root.val)
            return max(dfs(root.left, 2 * num, level + 1),
                       dfs(root.right, 2* num + 1, level + 1),
                       root.val - leftmost[level - 1])
    
        leftmost = []
        return dfs(root, 1, 1) + 1
