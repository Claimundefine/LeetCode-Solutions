class Solution:
    def minSwaps(self, data: List[int]) -> int:
        onesCount = sum(data)
        
        if onesCount <= 1:
            return 0
        
        maxCount = 0
        curCount = 0
        
        l, r = 0, 0
        
        while r < len(data):
            if data[r] == 1:
                curCount += 1
            if r - l + 1 > onesCount:
                if data[l] == 1:
                    curCount -= 1
                l += 1
            maxCount = max(maxCount, curCount)
            r += 1
            
        return onesCount - maxCount