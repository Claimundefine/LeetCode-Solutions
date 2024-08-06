class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        maxValue = nums[0]
        
        ans = [nums[0] * 2]
        
        for i in range(1,len(nums)):
            maxValue = max(maxValue, nums[i])
            ans.append(nums[i] + maxValue + ans[i-1])
            
        return ans