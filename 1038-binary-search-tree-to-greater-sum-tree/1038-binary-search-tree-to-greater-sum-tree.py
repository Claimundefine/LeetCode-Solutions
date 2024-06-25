# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        lesser = [0]
        
        def helper(helperRoot):
            if not helperRoot:
                return
            helper(helperRoot.right)
            curVal = helperRoot.val
            helperRoot.val += lesser[0]
            lesser[0] += curVal
            helper(helperRoot.left)
        
        helper(root)
            
        return root