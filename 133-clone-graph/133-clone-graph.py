"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        cloned = {}
        
        def dfs(node):
            if node in cloned:
                return cloned[node]
            
            newNode = Node(node.val)
            
            cloned[node] = newNode
            
            for neighbor in node.neighbors:
                newNode.neighbors.append(dfs(neighbor))
            return newNode
                    
        return dfs(node) if node else None
            
        