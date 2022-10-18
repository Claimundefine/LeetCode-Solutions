class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        
        cur = int(current[0:2]) * 60 + int(current[3:])
        cor = int(correct[0:2]) * 60 + int(correct[3:])
        
        actions = 0
        
        while cur < cor:
            if cur + 60 <= cor:
                cur += 60
            elif cur + 15 <= cor:
                cur += 15
            elif cur + 5 <= cor:
                cur += 5
            else:
                cur += 1
            actions += 1
    
        return actions