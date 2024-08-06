class Solution:
    def minimumPushes(self, word: str) -> int:
        hashmap = {}
        
        for char in word:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
            
        heap = []
        
        for key in hashmap:
            heap.append(-1 * hashmap[key])
            
        heapq.heapify(heap)
        
        press = 0
        letters = 0
        
        while heap:
            curNum = heapq.heappop(heap)
            press += (letters // 8  + 1) * curNum * -1
            letters += 1
            
        return press