# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lv = 1
        l = root.left
        while l:
            l = l.left
            lv += 1
        rv = 1
        r = root.right
        while r:
            r = r.right
            rv += 1
        if lv == rv:
            return pow(2, lv) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)