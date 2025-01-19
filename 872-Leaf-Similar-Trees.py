# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.L1 = []
        self.L2 = []
        def dfs(root, leafs):
            if not root:
                return
            if not root.left and not root.right:
                leafs.append(root.val)
            else:
                dfs(root.left, leafs)
                dfs(root.right, leafs)
        dfs(root1, self.L1)
        dfs(root2, self.L2)
        return self.L1 == self.L2