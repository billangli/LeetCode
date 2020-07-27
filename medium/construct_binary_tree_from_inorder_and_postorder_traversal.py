# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        
        mid = postorder[-1]
        mid_index = inorder.index(mid)
        left_length = mid_index
        right_length = len(inorder) - left_length - 1
        
        left = self.buildTree(inorder[:left_length], postorder[:left_length])
        right = self.buildTree(inorder[left_length+1:], postorder[left_length:-1])
        return TreeNode(mid, left=left, right=right)
