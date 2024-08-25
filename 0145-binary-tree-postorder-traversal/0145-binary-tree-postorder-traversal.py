# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        arr = []
        
        def function(root):
            if root.left:
                function(root.left)
            if root.right:
                function(root.right)
            arr.append(root.val)
            
        function(root)
        return arr
        