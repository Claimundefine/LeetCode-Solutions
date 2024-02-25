class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            directions = [[0,1],[1,0],[-1,0],[0,-1]]

            while q:
                curRow, curCol = q.pop()
                for direction in directions:
                    addRow = curRow + direction[0]
                    addCol = curCol + direction[1]
                    if addRow in range(row) and addCol in range(col) and grid[addRow][addCol] == "1":
                        q.append((addRow, addCol))
                        grid[addRow][addCol] = "0"
                

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1

        return islands