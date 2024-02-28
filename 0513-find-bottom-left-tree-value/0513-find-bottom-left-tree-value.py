# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = []
        
        q.append(root)
        
        leftMost = 0
        
        while q:
            leftMost = q[0].val
            for i in range(len(q)):
                curNode = q.pop(0)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
                    
        return leftMost