# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre_index = 0
        post_index = 0

        def dfs():
            nonlocal pre_index, post_index
            root = TreeNode(preorder[pre_index])
            pre_index += 1
            if root.val != postorder[post_index]:
                root.left = dfs()
            if root.val != postorder[post_index]:
                root.right = dfs()
            post_index += 1
            return root
        
        return dfs()
        