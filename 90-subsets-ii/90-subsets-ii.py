class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        def dfs(i,sub):
            if i >= len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            dfs(i+1, sub)
            
            sub.pop()
            
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
                
            dfs(i+1, sub)
            
        dfs(0, [])
        return res