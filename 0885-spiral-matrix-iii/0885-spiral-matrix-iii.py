class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        curR, curC = rStart, cStart
        curVal = 2

        numMove = 0
        
        numShift = 1
        
        direction = "L"
        
        ans = []
        ans.append([curR, curC])
        
        while curVal <= rows * cols:
            numMove += 1
            if direction == "L":
                curC += 1
                if curR in range(rows) and curC in range(cols):
                    ans.append([curR, curC])
                    curVal += 1
                if numMove == numShift:
                    direction = "D"
                    numMove = 0
            elif direction == "D":
                curR += 1
                if curR in range(rows) and curC in range(cols):
                    ans.append([curR, curC])
                    curVal += 1
                if numMove == numShift:
                    direction = "R"
                    numShift += 1
                    numMove = 0
            elif direction == "R":
                curC -= 1
                if curR in range(rows) and curC in range(cols):
                    ans.append([curR, curC])
                    curVal += 1
                if numMove == numShift:
                    direction = "U"
                    numMove = 0
            else:
                curR -= 1
                if curR in range(rows) and curC in range(cols):
                    ans.append([curR, curC])
                    curVal += 1
                if numMove == numShift:
                    direction = "L"
                    numShift += 1
                    numMove = 0
                    
        return ans