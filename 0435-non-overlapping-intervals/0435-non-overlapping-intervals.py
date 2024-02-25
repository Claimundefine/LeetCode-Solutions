class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        
        print(intervals)
        
        ans = []
        
        i = 0
        
        while i < len(intervals):
            curInterval = intervals[i]
            ans.append(curInterval)
            i += 1
            while i < len(intervals) and intervals[i][0] < curInterval[1]:
                i += 1
                
        return len(intervals) - len(ans)