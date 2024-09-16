class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = set()
        
        for time in timePoints:
            arr = time.split(":")
            minsTime = 60 * int(arr[0]) + int(arr[1])
            if minsTime in times:
                return 0
            times.add(minsTime)
            
        times = list(times)
        
        times.sort()
        
        minTime = float("inf")
        
        for i in range(len(times) -1):
            minTime = min(minTime, times[i+1] - times[i])
            
        timeToZero = 24 * 60 - times[-1]
            
        minTime = min(minTime, timeToZero + times[0])
        
        return minTime