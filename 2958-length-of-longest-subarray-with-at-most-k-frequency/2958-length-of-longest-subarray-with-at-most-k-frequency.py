class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        curLen = 0
        
        l = 0
        
        hashmap = {}
        
        for i in range(len(nums)):
            curVal = nums[i]
            
            if curVal not in hashmap:
                hashmap[curVal] = 0
            hashmap[curVal] += 1
            
            if hashmap[curVal] > k:
                while nums[l] != curVal:
                    hashmap[nums[l]] -= 1
                    l += 1
                hashmap[nums[l]] -= 1
                l += 1
            curLen = max(curLen, i - l + 1)
            
        return curLen