class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        ans = 0
        
        l, r = 0, 0
        
        hashmap = {}
        
        while r < len(nums):
            if nums[r] not in hashmap:
                hashmap[nums[r]] = 0
            hashmap[nums[r]] += 1
            if len(hashmap) == len(uniqueNums):
                while len(hashmap) == len(uniqueNums):
                    hashmap[nums[l]] -= 1
                    if hashmap[nums[l]] == 0:
                        del hashmap[nums[l]]
                    l += 1
                    
            ans += l
            r += 1
            
            
        return ans