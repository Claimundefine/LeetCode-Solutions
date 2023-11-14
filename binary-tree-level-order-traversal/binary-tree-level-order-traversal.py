# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        ans = []
        
        q = collections.deque()
        
        q.append(root)
        
        while q:
            curLevel = []
            
            for i in range(len(q)):
                curNode = q.popleft()
                curLevel.append(curNode.val)
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
            ans.append(curLevel)
            
        return ans
            