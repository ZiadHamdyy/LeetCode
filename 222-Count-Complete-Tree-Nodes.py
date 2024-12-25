# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def counter(root):
            if not root:
                return 0
            counter(root.left)
            self.count += 1
            counter(root.right)
        counter(root)
        return self.count