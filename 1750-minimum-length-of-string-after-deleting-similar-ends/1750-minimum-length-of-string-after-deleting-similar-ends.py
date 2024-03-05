class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        
        while l < r:
            curLeft = s[l]
            curRight = s[r]
            if curLeft != curRight:
                break
            if l + 1 == r:
                return 0
            l += 1
            r -= 1
            while curLeft == s[l] and l + 1 != r:
                l += 1
            while curLeft == s[r] and r - 1 != l:
                r -= 1
            
        return r - l + 1