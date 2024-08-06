class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if source == target:
            return 0
        
        adjList = {}

        for i in range(len(routes)):
            for val in routes[i]:
                if val not in adjList:
                    adjList[val] = []
                adjList[val].append(i)
        
        if target not in adjList or source not in adjList:
            return -1
                

        def bfs():
            queue = collections.deque()
            visited = set()
            for route in adjList[source]:
                visited.add(route)
                queue.append(route)
            level = 0

            while queue:
                level += 1
                for i in range(len(queue)):
                    curRoute = queue.popleft()
                    if curRoute in adjList[target]:
                        return level
                    for busStop in routes[curRoute]:
                        for route in adjList[busStop]:
                            if route not in visited:
                                visited.add(route)
                                queue.append(route)  
            
            return -1


        return bfs()