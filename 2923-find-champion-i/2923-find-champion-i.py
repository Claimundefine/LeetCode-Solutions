class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)):
            isChampion = True
            for j in range(len(grid)):
                if i == j:
                    continue
                if grid[i][j] == 0:
                    isChampion = False
                    break
            if isChampion:
                return i
        