class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        
        hashmap = {}
        
        hashmap["("], hashmap["{"], hashmap["["] = True, True, True
        hashmap[")"], hashmap["}"], hashmap["]"] = "(","{", "["
        
        for char in s:
            if hashmap[char] == True:
                arr.append(char)
            else:
                if arr == []:
                    return False
                if arr[-1] == hashmap[char]:
                    arr.pop()
                else:
                    return False
            
        if not arr:
            return True
        
        return False