class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hashmap = {}
        hashmap[5] = 0
        hashmap[10] = 0
        hashmap[20] = 0
        
        for num in bills:
            hashmap[num] += 1
            if num == 10:
                if hashmap[5] == 0:
                    return False
                hashmap[5] -= 1
            if num == 20:
                if hashmap[5] > 0 and hashmap[10] > 0:
                    hashmap[5] -= 1
                    hashmap[10] -= 1
                elif hashmap[5] >= 3:
                    hashmap[5] -= 3
                else:
                    return False
                
        return True