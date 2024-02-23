class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cheapest = [-1]
        
        flightMap = {}
        
        visited = {}
        
        for flight in flights:
            if flight[0] not in flightMap:
                flightMap[flight[0]] = []
            flightMap[flight[0]].append((flight[2], flight[1]))
            
        li = [(0,0,src)]
        
        heapq.heapify(li)
        
        while li:
            cost, step, cur = heapq.heappop(li)
            if (cur in visited and step > visited[cur]) or  step > k + 1:
                continue
            if cur == dst:
                return cost
            visited[cur] = step
            if cur in flightMap:
                for newCost, newCur in flightMap[cur]:
                    heapq.heappush(li, (cost + newCost, step + 1, newCur))
                
                
        return -1
            