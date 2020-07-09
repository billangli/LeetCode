# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        def getExtremities(root: TreeNode) -> List[List[int]]:
            """
            Return a list of list of two ints
            The outer list is the level of the list in reverse, where the last item is root
            The inner list is the leftmost and rightmost node in that level
            Leftmost is 0 and rightmost is 2^level - 1
            """
            if root is None:
                return []
            
            left_result = getExtremities(root.left)
            right_result = getExtremities(root.right)
            
            i = len(left_result) - 1
            j = len(right_result) - 1
            level = 0
            result_len = max(len(left_result), len(right_result))
            result = [[] for _ in range(result_len + 1)]
            
            result[-1] = [0, 0]
            while i >= 0 or j >= 0:
                padding = 2 ** level
                leftmost = left_result[i][0] if i >= 0 else right_result[j][0] + padding
                rightmost = left_result[i][1] if j < 0 else right_result[j][1] + padding
                result[result_len - level - 1] = [leftmost, rightmost]
                i -= 1
                j -= 1
                level += 1
                
            return result
        
        extremities = getExtremities(root)
        max_ = 0
        for list_ in extremities:
            diff = list_[1] - list_[0] + 1
            if max_ < diff:
                max_ = diff
        return max_
                
