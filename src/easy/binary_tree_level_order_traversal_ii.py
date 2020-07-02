# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = [root]
        while len(queue) > 0:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level != []:
                result.insert(0, level)
        return result
