class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        count = 0
        
        curPoint = 0
        
        while curPoint < len(points):
            rightMost = points[curPoint][1]
            curPoint += 1
            while curPoint < len(points) and points[curPoint][0] <= rightMost:
                rightMost = min(rightMost, points[curPoint][1])
                curPoint += 1
            count += 1
            
        return count
                    