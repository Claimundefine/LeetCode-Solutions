class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        rooms = [0]
        
        heapq.heapify(rooms)
        
        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms,interval[1])
            else:
                heapq.heappush(rooms,interval[1])
                
        return len(rooms)