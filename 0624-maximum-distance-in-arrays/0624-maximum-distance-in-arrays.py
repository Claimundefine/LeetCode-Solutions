class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        distance = 0
        high = float("-inf")
        low = float("inf")
        
        for i in range(len(arrays)):
            curLow = arrays[i][0]
            curHigh = arrays[i][-1]
            if i > 0:
                distance = max(abs(high-curLow), abs(low-curHigh), distance)
            high = max(high, curHigh)
            low = min(low, curLow)
                
        return distance