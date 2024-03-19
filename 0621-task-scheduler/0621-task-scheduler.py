class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashmap = {}
        
        for task in tasks:
            if task not in hashmap:
                hashmap[task] = 0
            hashmap[task] += 1
            
        arr = []
            
        for key in hashmap:
            arr.append((hashmap[key] * -1, key))
            
        intervals = 0
        
        heapq.heapify(arr)
        
        print(arr)
        
        while arr:
            curIteration = []
            
            while arr and len(curIteration) < n + 1:
                curIteration.append(heapq.heappop(arr))
            
            for val in curIteration:
                if val[0] < -1:
                    heapq.heappush(arr, (val[0] + 1 , val[1]))
            print(arr)
            
            if not arr:
                return intervals + len(curIteration)
            intervals += n + 1
                
        