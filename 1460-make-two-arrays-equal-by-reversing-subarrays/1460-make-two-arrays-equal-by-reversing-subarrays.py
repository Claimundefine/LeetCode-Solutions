class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        hash1, hash2 = {}, {}
        
        for num in target:
            if num not in hash1:
                hash1[num] = 0
            hash1[num] += 1
        
        for num in arr:
            if num not in hash2:
                hash2[num] = 0
            hash2[num] += 1
            
        return hash1 == hash2