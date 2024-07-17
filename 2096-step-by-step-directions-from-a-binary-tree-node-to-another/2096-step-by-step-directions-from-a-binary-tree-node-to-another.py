# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # Build an adjacency list with parents
        # once I find both nodes, do a DFS from startValue
        
        adj = {}
        
        q = deque()
        
        q.append((root, None))
        
        while q:
            curNode, parent = q.popleft()
            curVal = curNode.val
                 
            adj[curVal] = []
            
            if parent is not None:
                adj[curVal].append((parent, "U"))
                
            if curNode.left:
                adj[curVal].append((curNode.left.val, "L"))
                q.append((curNode.left, curVal))
                
            if curNode.right:
                adj[curVal].append((curNode.right.val, "R"))
                q.append((curNode.right, curVal))
                
                
        queue = deque([(startValue, "")])
        visited = set([startValue])
    
        while queue:
            cur, path = queue.popleft()
        
            if cur == destValue:
                return path
        
            for neighbor, direction in adj[cur]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + direction))
    
        return ""
            
            