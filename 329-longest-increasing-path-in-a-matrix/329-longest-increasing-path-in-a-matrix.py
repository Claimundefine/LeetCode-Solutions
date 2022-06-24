class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        
        dp = {}
        
        def dfs(r, c, prev):
            if (r<0 or r == ROW or
            c<0 or c==COL or 
            matrix[r][c] <= prev):
                return 0
            
            if (r,c) in dp:
                return dp[(r,c)]
            
            cur = matrix[r][c]
            
            res = 1
            res = max(res, 1+dfs(r+1, c, cur))
            res = max(res, 1 + dfs(r-1, c, cur))
            res = max(res, 1+dfs(r, c+1, cur))
            res = max(res, 1+dfs(r, c-1, cur))
            
            dp[(r,c)] = res
            
            return res
        
        for i in range(ROW):
            for j in range(COL):
                dfs(i,j,-1)
                
        return max(dp.values())