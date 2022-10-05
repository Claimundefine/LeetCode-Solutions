class Solution:
    def romanToInt(self, s: str) -> int:
        
        rnum = {}
        rnum["I"] = 1
        rnum["V"] = 5
        rnum["X"] = 10
        rnum["L"] = 50
        rnum["C"] = 100
        rnum["D"] = 500
        rnum["M"] = 1000

        bnum = {}
        bnum["I"] = "VX"
        bnum["X"] = "LC"
        bnum["C"] = "DM"
        
        totalValue = 0

        for i in range(len(s)):
            totalValue += rnum[s[i]]

            if i > 0 and s[i-1] in bnum:
                if s[i] in bnum[s[i-1]]:
                    totalValue -= rnum[s[i-1]] * 2

        return totalValue
        
        
        