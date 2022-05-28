class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        currArr = [0] * n
        
        memoization = [currArr for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    memoization[i][j] = 1
                else:
                    memoization[i][j] = memoization[i-1][j] + memoization[i][j-1]
                    
        return memoization[m-1][n-1]