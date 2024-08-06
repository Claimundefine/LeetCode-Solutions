class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        length = len(rooms)
        width = len(rooms[0])
        
        q = deque()
        
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                print(i, j)
                if rooms[i][j] == 0:
                    q.append((i,j))
        
        dist = 0
        
        while q:
            dist += 1
            directions = [[1,0], [0,1], [-1,0], [0,-1]]
            
            for i in range(len(q)):
                curR, curC = q.popleft()
                for dirR, dirC in directions:
                    newR = curR + dirR
                    newC = curC + dirC
                    
                    if (newR in range(length) and
                       newC in range(width) and 
                        rooms[newR][newC] == 2147483647):
                        rooms[newR][newC] = dist
                        q.append((newR, newC))
                        
                        