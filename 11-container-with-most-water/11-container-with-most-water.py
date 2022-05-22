class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        leftIdx = 0
        rightIdx = len(height) - 1
        
        
        while leftIdx < rightIdx:
            if (rightIdx-leftIdx) * min(height[leftIdx], height[rightIdx]) > maxArea:
                maxArea = (rightIdx-leftIdx) * min(height[leftIdx], height[rightIdx])
            if height[leftIdx] > height[rightIdx]:
                rightIdx -= 1
            else:
                leftIdx += 1
        
        return maxArea
        