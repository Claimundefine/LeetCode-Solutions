class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        
        workersMap = {}
        
        bikesTaken = [-1] * (len(bikes))
        
        workBike = [-1] * len(workers)
        
        heap = []
        
        for i in range(len(workers)):
            wX, wY = workers[i][0], workers[i][1]
            
            distances = []
            
            for j in range(len(bikes)):
                bX, bY = bikes[j]
                
                distance = abs(wX - bX) + abs(wY - bY)
                distances.append((distance, i, j))
            
            distances.sort(reverse=True)
            heapq.heappush(heap, distances.pop())
            workersMap[i] = distances
        while heap:
            _, curW, curB = heapq.heappop(heap)
            if bikesTaken[curB] == -1:
                bikesTaken[curB] = curW
                workBike[curW] = curB
            else:
                heapq.heappush(heap, workersMap[curW].pop())
                
        return workBike
            