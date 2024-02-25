class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        robot1Reachable = set()
        robot2Reachable = set()

        row = len(grid)
        col = len(grid[0])

        maxVal = 0
        j = 0
        for i in range(len(grid)):
            j += 1
            for k in range(j):
                if k < (len(grid[0])):
                    robot1Reachable.add((i,k))

        j = 0

        for i in range(len(grid)):
            j += 1
            for k in range(j):
                if 0 <= len(grid[0]) - 1 - k:
                    robot2Reachable.add((i, col - 1 - k))


        dp = {}

        dp[(0, 0, col-1)] = grid[0][0] + grid[0][col - 1]

        upper = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]

        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                for k in range(len(grid[0])):
                    if not ((i,j) in robot1Reachable and (i,k) in robot2Reachable):
                        continue
                    dp[(i,j,k)] = 0
                    for c1, c2 in upper:
                        robot1Pos = j + c1
                        robot2Pos = k + c2
                        if ((i-1, robot1Pos) in robot1Reachable 
                        and (i-1, robot2Pos) in robot2Reachable):
                            if j == k:
                                dp[(i,j,k)] = max(dp[(i,j,k)], dp[(i-1, robot1Pos, robot2Pos)] + grid[i][j])
                            else:
                                dp[(i,j,k)] = max(dp[(i,j,k)], dp[(i-1, robot1Pos, robot2Pos)] + grid[i][j] + grid[i][k])
                    if i == len(grid) - 1:
                        maxVal = max(maxVal, dp[(i,j,k)])

        return maxVal

