class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        curCount = 0
        
        hashmap = {}
        hashmap[0] = -1
        
        maxVal = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                curCount -= 1
            else:
                curCount += 1
            if curCount not in hashmap:
                hashmap[curCount] = i
            else:
                maxVal = max(maxVal, i - hashmap[curCount])
                
        return maxVal