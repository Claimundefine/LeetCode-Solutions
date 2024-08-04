class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        total = []
        
        for i in range(len(nums)-1):
            curVal = nums[i]
            total.append(curVal)
            curTotal = curVal
            for j in range(i + 1, len(nums)):
                curTotal += nums[j]
                total.append(curTotal)
                
        total.append(nums[len(nums)-1])
        
        total.sort()
        
        ans = 0
        
        for i in range(left-1, right):
            ans += total[i]
            
        return ans % (10**9 + 7)