class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = float("-inf")  
        window_sum = float("-inf")
        for x in nums:
            window_sum = max(window_sum + x, x)
            best_sum = max(window_sum, best_sum)
        return best_sum