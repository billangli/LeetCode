# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def traverse(root: TreeNode, sums: List[int]) -> int:
            result = 0
            new_sums = [sum]
            for s in sums:
                diff = s - root.val
                if diff == 0: result += 1
                new_sums.append(diff)
            if root.left: 
                result += traverse(root.left, new_sums) 
            if root.right: 
                result += traverse(root.right, new_sums)
            return result
            
        return traverse(root, [sum])
