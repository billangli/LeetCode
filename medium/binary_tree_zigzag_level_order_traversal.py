# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        level = 0
        queue = [root]
        temp = []
        while len(queue) > 0:
            node = queue.pop()
            if node is not None:
                if len(result) <= level:
                    result.append([node.val])
                else:
                    result[level].append(node.val)
                
                if level % 2 == 0:
                    temp.append(node.left)
                    temp.append(node.right)
                else:
                    temp.append(node.right)
                    temp.append(node.left)
            if len(queue) == 0:
                queue = temp
                temp = []
                level += 1
        return result
