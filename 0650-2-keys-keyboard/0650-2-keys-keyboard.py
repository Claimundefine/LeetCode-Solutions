class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        dp = [x for x in range(n+1)]
        
        dp[1] = 1
        
        for i in range(2, n+1):
            for j in range(1, i//2 + 1):
                if i % j == 0:
                    print(i, j, i // j)
                    divisor = i // j
                    dp[i] = min(dp[i], dp[j] + divisor)

        return dp[-1]
                