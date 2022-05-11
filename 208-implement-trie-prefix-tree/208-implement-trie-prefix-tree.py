class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curNode = self.root
        for char in word:
            if char not in curNode.children:
                curNode.children[char] = TrieNode()
            curNode = curNode.children[char]
        curNode.end = True
        

    def search(self, word: str) -> bool:
        curNode = self.root
        for char in word:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False
            
        return curNode.end
        

    def startsWith(self, prefix: str) -> bool:
        curNode = self.root
        for char in prefix:
            if char in curNode.children:
                curNode = curNode.children[char]
            else:
                return False 
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)