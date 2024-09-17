class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        a1 = s1.split(" ")
        a2 = s2.split(" ")
        set1 = {}
        set2 = {}
        
        list1 = []
        list2 = []
        
        for val in a1:
            if val not in set1:
                set1[val] = 0
            set1[val] += 1
            
        for val in a2:
            if val not in set2:
                set2[val] = 0
            set2[val] += 1
            
        for key in set1:
            if set1[key] == 1:
                list1.append(key)
        
        for key in set2:
            if set2[key] == 1:
                list2.append(key)
        
        
        return [x for x in list1 if x not in set2] + [x for x in list2 if x not in set1]
    
    