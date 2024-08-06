class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if not asteroids:
            return []
        
        stack = []

        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i])
            elif asteroids[i] < 0:
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                elif (stack and stack[-1] < 0) or not stack:
                    stack.append(asteroids[i])
                #Else do nothing, asteroid is bigger
            else:
                stack.append(asteroids[i])
                
        return stack