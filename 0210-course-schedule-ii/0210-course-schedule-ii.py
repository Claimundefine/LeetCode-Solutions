class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        adjList = {}
        ordering = []
        
        for course1, course2 in prerequisites:
            if course2 not in adjList:
                adjList[course2] = []
            adjList[course2].append(course1)
            inDegree[course1] += 1
        
        q = deque()
        visited = set()
        
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            curCourse = q.popleft()
            visited.add(curCourse)
            ordering.append(curCourse)
            
            if curCourse in adjList:
                for course in adjList[curCourse]:
                    inDegree[course] -= 1
                    if inDegree[course] == 0:
                        q.append(course)
        
        if len(ordering) != numCourses:
            return []
        
        return ordering