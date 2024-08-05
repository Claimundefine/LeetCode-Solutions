class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashmap = {}
        
        for val in arr:
            if val not in hashmap:
                hashmap[val] = 0
            hashmap[val] += 1
            
        for val in arr:
            if hashmap[val] == 1:
                k -= 1
            if k == 0:
                return val
            
        return ""