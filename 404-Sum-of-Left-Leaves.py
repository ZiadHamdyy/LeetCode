# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        def dfs(root, left):
            if not root:
                return
            dfs(root.left, True)
            dfs(root.right, False)
            if not root.left and not root.right and left:
                self.total += root.val
        dfs(root, False)
        return self.total