class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        r = len(grid)
        c = len(grid[0])
        
        maxMinutes = 0
        oranges = 0
        
        q = []
        
        #adding all rotten oranges to queue
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                elif grid[i][j] == 1:
                    oranges += 1
                    
        while q:
            qr, qc, mins = q.pop(0)
            
            directions = [[1,0], [-1, 0], [0,1], [0, -1]]
            
            for dr, dc in directions:
                newR = qr + dr
                newC = qc + dc
                if (newR in range(r) and
                newC in range(c) and
                grid[newR][newC] == 1):
                    oranges -= 1
                    grid[newR][newC] = 2
                    q.append((newR, newC, mins + 1))
                    if mins + 1 > maxMinutes:
                        maxMinutes = mins + 1
            
            grid[qr][qc] = 0
            
        if oranges != 0:
            return -1
            
        return maxMinutes