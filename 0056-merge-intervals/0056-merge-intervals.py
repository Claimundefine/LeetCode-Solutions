class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])

        ans = []
        
        i = 0
        
        while i < len(intervals):
            curInterval = intervals[i]
            i += 1
            while i < len(intervals) and intervals[i][0] <= curInterval[1]:
                curInterval[1] = max(curInterval[1], intervals[i][1])
                i += 1
            ans.append(curInterval)
            
        return ans