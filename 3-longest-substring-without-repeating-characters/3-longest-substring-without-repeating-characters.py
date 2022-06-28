class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        leftIdx = 0
        rightIdx = 0
        
        dict = {}
        
        for i in range(len(s)):
            rightIdx += 1
            if s[i] not in s[leftIdx:rightIdx-1]:
                if rightIdx - leftIdx > longestLength:
                    longestLength = rightIdx - leftIdx
            else:
                leftIdx = dict[s[i]] + 1
            dict[s[i]] = i
            
        return longestLength