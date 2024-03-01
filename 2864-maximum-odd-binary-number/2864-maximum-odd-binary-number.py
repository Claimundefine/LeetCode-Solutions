class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        numZeros = 0
        numOnes = 0
        
        for char in s:
            if char == "0":
                numZeros += 1
            else:
                numOnes += 1
                
        ans = ""
        
        for i in range(numOnes - 1):
            ans += "1"
        
        for j in range(numZeros):
            ans += "0"
            
        return ans + "1"