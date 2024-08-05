class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        
        for val in nums:
            temp = rob2
            rob2 = max(rob1 + val, rob2)
            rob1 = temp
        
        return max(rob1, rob2)