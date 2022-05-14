class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        longest = 0
        
        for num in numSet:
            if num - 1 in numSet:
                continue
            curSequence = 1
            curVal = num
            while (curVal + 1) in numSet:
                curSequence += 1
                curVal += 1
            longest = max(longest, curSequence)
            
        return longest