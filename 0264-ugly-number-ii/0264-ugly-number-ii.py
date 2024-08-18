class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        heap = [2,3,5]
        heapq.heapify(heap)
        curVal = 0
        seen = set()
        
        for i in range(1, n):
            curVal = heapq.heappop(heap)
            if curVal * 2 not in seen:
                heapq.heappush(heap, curVal * 2)
                seen.add(curVal * 2)
            if curVal * 3 not in seen:
                heapq.heappush(heap, curVal * 3)
                seen.add(curVal * 3)
            if curVal * 5 not in seen:
                heapq.heappush(heap, curVal * 5)
                seen.add(curVal * 5)

        return curVal