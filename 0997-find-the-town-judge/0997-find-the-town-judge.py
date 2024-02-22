class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        if n == 1:
            return 1
        trustMap = {}
        
        isTrust = set()
        
        for i in range(1, n + 1):
            isTrust.add(i)
            
        for a, b in trust:
            if a in isTrust:
                isTrust.remove(a)
            if b not in trustMap:
                trustMap[b] = set()
            trustMap[b].add(a)
            
        if len(isTrust) == 1:
            for key in isTrust:
                if key in trustMap and len(trustMap[key]) == n - 1:
                    return key
                
        return -1