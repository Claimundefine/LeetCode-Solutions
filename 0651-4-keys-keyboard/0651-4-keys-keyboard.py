class Solution:
    def maxA(self, n: int) -> int:
        dp = [ x for x in range(n+1)]
        
        for i in range(5, n+1):
            for j in range(1, i - 3):
                dp[i] = max(dp[i], dp[i-2-j] * (1+j))
                
        return dp[-1]