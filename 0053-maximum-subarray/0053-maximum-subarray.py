class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float("-inf")  
        window_sum = float("-inf")
        for i in range(len(nums)):
            window_sum = max(nums[i], window_sum + nums[i])
            best_sum = max(best_sum, window_sum)
            
        return best_sum