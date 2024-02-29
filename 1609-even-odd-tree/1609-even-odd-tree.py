# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = collections.deque()
        
        q.append(root)
        
        curLevel = 0
        while q:
            prevVal = -1
            for i in range(len(q)):
                curNode = q.popleft()
                if i == 0:
                    prevVal = curNode.val
                    if curLevel % 2 == prevVal % 2:
                        return False
                else: 
                    if curLevel % 2 == 1:
                        if curLevel % 2 == curNode.val % 2 or curNode.val >= prevVal:
                            return False
                        prevVal = curNode.val
                    else:
                        if curLevel % 2 == curNode.val % 2 or curNode.val <= prevVal:
                            return False
                        prevVal = curNode.val
                if curNode.left:
                    q.append(curNode.left)
                if curNode.right:
                    q.append(curNode.right)
                
            curLevel += 1
        
        return True