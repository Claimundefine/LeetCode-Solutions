class TrieNode:
    def __init__(self):
        self.children = {}
        
        
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = TrieNode()
        arr1 = [str(x) for x in arr1]
        arr2 = [str(x) for x in arr2]
    
        def addToTrie(val):
        
            cur = trie
        
            for char in val:
                if char not in cur.children:
                    cur.children[char] = TrieNode()
                cur = cur.children[char]
    
        for val in arr1:
            addToTrie(val)
        
        maxVal = 0
    
        for val in arr2:
            cur = trie
        
            for i in range(len(val)):
                if val[i] not in cur.children:
                    break
                maxVal = max(maxVal, i + 1)
                cur = cur.children[val[i]]
            
        return maxVal