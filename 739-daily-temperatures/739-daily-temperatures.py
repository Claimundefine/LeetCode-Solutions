class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = []
        
        ans = [0] * len(temperatures)
        
        i = 1
        
        q.append(0)
        
        while i < len(temperatures):
            while q and temperatures[q[-1]] < temperatures[i]:
                ans[q[-1]] = i - q[-1]
                q.pop()
            q.append(i)
            i += 1
            
        return ans