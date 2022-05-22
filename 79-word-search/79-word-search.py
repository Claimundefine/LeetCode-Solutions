class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        root = TrieNode()
        
        root.addWord(word)
        
        visited = set()
        
        exist = [False]
        
        numRow, numCol = len(board), len(board[0])
        
        def dfs(r, c, node, prefix):
            if (r < 0 or c < 0 or 
               r == numRow or c == numCol
               or board[r][c] not in node.children or (r,c) in visited):
                return
            
            visited.add((r,c))
            prefix += board[r][c]
            node = node.children[board[r][c]]
            
            if node.isWord:
                exist[0] = True
                
            dfs(r-1, c, node, prefix)
            dfs(r+1, c,node, prefix)
            dfs(r, c-1, node, prefix)
            dfs(r, c+1, node, prefix)
            
            visited.remove((r,c))
        
        for i in range(numRow):
            for j in range(numCol):
                dfs(i, j, root, "")
                if exist[0] == True:
                    return True
                
        return exist[0]
            