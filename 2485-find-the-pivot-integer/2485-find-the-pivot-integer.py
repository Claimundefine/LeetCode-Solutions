class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1
        
        consecutive = n * (n + 1) / 2
        cur = 1
        
        for i in range(2, n + 1):
            cur += i
            consecutive -= (i-1)
            if cur == consecutive:
                return i
            elif cur > consecutive:
                return -1
            
        return -1