class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if 1 <= n <= 2:
            return 1
        
        memoization = [-1] * (n+1)
        memoization[0] = 0
        memoization[1] = 1
        memoization[2] = 1
        
        for i in range(3,n+1):
            memoization[i] = memoization[i-1] + memoization[i-2] + memoization[i-3]
            
        return memoization[n]
        
        