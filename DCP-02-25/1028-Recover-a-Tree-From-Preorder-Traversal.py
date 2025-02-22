# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        self.index = 0
        return self.dsf(traversal, 0)

    def dsf(self, traversal: str, depth: int) -> Optional[TreeNode]:
        start = self.index
        d = 0

        while self.index < len(traversal) and traversal[self.index] == '-':
            d += 1
            self.index += 1
        if d != depth:
            self.index = start
            return None

        val = 0
        while self.index < len(traversal) and traversal[self.index].isdigit():
            val = val * 10 + int(traversal[self.index])
            self.index += 1

        node = TreeNode(val)
        node.left = self.dsf(traversal, depth + 1)
        node.right = self.dsf(traversal, depth + 1)

        return node