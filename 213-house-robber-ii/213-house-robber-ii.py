class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        def robber1(nums):
            rob1, rob2 = 0, 0
            
            for num in nums:
                temp = max(rob1 + num, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(robber1(nums[0:len(nums)-1]), robber1(nums[1:]))