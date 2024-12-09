144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        lis = []
        def preorder(root):
            if root == None:
                return
            lis.append(root.val)
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return lis
        