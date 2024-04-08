class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        firstChar = False
        count = 0
        
        for i in range(-1, len(s) * (-1) - 1, -1):
            if not firstChar and s[i] != " ":
                firstChar = True
                count += 1
            elif firstChar:
                if s[i] == " ":
                    return count
                count += 1
                
        return count