class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        for i in range(len(nums)):
            curVal = abs(nums[i])
            if nums[curVal] < 0:
                return curVal
            nums[curVal] *= -1
            
        return -1