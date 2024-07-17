# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        trees = set()
        to_delete = set(to_delete)
        
        trees.add(root)
        
        def dfs(root, parent, direction):
            if not root:
                return
            if root.val in to_delete:
                if direction == "L":
                    parent.left = None
                if direction == "R":
                    parent.right = None
                if root in trees:
                    trees.remove(root)
                if root.left:
                    trees.add(root.left)
                if root.right:
                    trees.add(root.right)
                    
            dfs(root.left, root, "L")
            dfs(root.right, root, "R")
            
        dfs(root, None, None)
            
        return list(trees)
            