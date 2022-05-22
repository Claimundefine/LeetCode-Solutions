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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = TrieNode()
        for word in words:
            trie.addWord(word)
            
        numRow, numCol = len(board), len(board[0])
        res = []
        visited = set()
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
               r == numRow or c == numCol
               or board[r][c] not in node.children or (r,c) in visited):
                return
            
            visited.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.append(word)
                node.isWord = False
            
            dfs(r-1, c, node, word)
            dfs(r+1, c, node, word)
            dfs(r, c-1, node, word)
            dfs(r, c+1, node, word)
            
            visited.remove((r,c))
        
        for i in range(numRow):
            for j in range(numCol):
                dfs(i, j, trie, "")
                
        return res