class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap1 = []
        
        heap2 = []
        
        hashmap = {}
        
        for i in range(len(capital)):
            if capital[i] not in hashmap:
                hashmap[capital[i]] = []
            hashmap[capital[i]].append(profits[i])
            
        for key in hashmap:
            heapq.heappush(heap1, (key, hashmap[key]))
        
        while heap1 and heap1[0][0] <= w:
            curCapital, curProfits = heapq.heappop(heap1)
            
            for profit in curProfits:
                heapq.heappush(heap2, profit * -1)
        
        while k > 0:
            k -= 1
            if not heap2:
                return w
            w += (heapq.heappop(heap2) * -1)
            
            while heap1 and heap1[0][0] <= w:
                curCapital, curProfits = heapq.heappop(heap1)
            
                for profit in curProfits:
                    heapq.heappush(heap2, profit * -1)
                
        return w
            