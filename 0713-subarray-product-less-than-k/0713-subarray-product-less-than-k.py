class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if len(nums) == 0:
            return 0
        
        cur = 1
        l = 0
        total = 0
        
        for i in range(len(nums)):
            cur *= nums[i]
            
            while cur >= k and l <= i:
                cur //= nums[l]
                l += 1
                
            total += i - l + 1
            
        return total