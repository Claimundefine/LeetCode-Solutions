# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        count = [0]
        
        def helper(node, maxVal):
            curVal = maxVal
            if not node:
                return
            if node.val >= maxVal:
                count[0] += 1
                curVal = node.val
            helper(node.left, curVal)
            helper(node.right, curVal)
        
        count[0] += 1
        
        helper(root.left, root.val)
        helper(root.right, root.val)
        
        return count[0]