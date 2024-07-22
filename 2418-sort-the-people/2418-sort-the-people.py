class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hashmap = {}
        
        for i in range(len(heights)):
            hashmap[heights[i]] = names[i]
            
        heights.sort(reverse=True)
        
        ans = []
        
        for i in range(len(heights)):
            ans.append(hashmap[heights[i]])
            
        return ans