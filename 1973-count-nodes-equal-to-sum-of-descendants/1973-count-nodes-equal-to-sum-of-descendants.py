# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        count = [0]
        
        def helper(root):
            if not root:
                return 0
            
            desc = helper(root.left) + helper(root.right)
            
            if root.val == desc:
                count[0] += 1
                
            return root.val + desc
        
        helper(root)
        
        return count[0]