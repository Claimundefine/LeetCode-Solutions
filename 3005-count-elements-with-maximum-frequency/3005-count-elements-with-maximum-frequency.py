class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        arr = [0] * 101
        
        for num in nums:
            arr[num] += 1
            
        highest = 0
        count = 0
        
        for val in arr:
            if val > highest:
                highest = val
                count = 1
            elif val == highest:
                count += 1
                
        return highest * count