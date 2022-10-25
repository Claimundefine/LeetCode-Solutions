class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        
        counter = 0
        ending = -1000000
        
        for interval in intervals:
            if interval[0] >= ending:
                counter += 1 
                ending = interval[1]
        
        return len(intervals) - counter