# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        grid = defaultdict(lambda: defaultdict(list))
        
        def traverse(node: TreeNode, x: int, y: int) -> None:
            """Traverses through the tree and places the values of nodes in the right grid entry"""
            if node is None:
                return
            
            grid[x][y].append(node.val)
            traverse(node.left, x - 1, y - 1)
            traverse(node.right, x + 1, y - 1)
            
        traverse(root, 0, 0)
        
        result = []
        for x_key in sorted(grid.keys()):
            column = []
            for y_key in sorted(grid[x_key].keys(), reverse=True):
                column.extend(sorted(grid[x_key][y_key]))
            result.append(column)
        return result
