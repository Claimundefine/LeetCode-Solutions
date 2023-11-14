# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(root, small, big):
            if not root:
                return True
            
            if root.val < small or root.val > big:
                return False
            
            return checkValid(root.left, small, root.val -1) and checkValid(root.right, root.val + 1, big)
            
        return checkValid(root,-4294967296, 4294967296)