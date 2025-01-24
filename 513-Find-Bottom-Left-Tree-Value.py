# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()

        queue.append(root)
        res = 0
        while queue:
            node = queue.popleft()
            if node:
                res = node.val
                queue.append(node.right)
                queue.append(node.left)
        return res