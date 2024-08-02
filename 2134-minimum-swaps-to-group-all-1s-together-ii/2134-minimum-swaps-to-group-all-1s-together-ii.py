class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        onesCount = sum(nums)
        
        if onesCount <= 1:
            return 0
        
        maxCount, curCount = 0, 0
        
        l, r = 0, 0
        
        while r < len(nums) * 2:
            curIdx = r % len(nums)
            
            if nums[curIdx] == 1:
                curCount += 1
            
            if r - l + 1 > onesCount:
                curCount -= nums[l%len(nums)]
                l += 1
            
            maxCount = max(maxCount, curCount)
                
            r += 1
            
        return onesCount - maxCount