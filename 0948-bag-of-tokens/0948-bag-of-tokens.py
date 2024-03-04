class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        
        tokens.sort()
        
        l, r = 0, len(tokens) - 1
        
        while l <= r:
            if power - tokens[l] >= 0:
                score += 1
                power -= tokens[l]
                l += 1
            else:
                leftTotal = 0
                rightTotal = 0
                if l + 1 < r and score > 0:
                    leftTotal = tokens[l] + tokens[l+1]
                    rightTotal = tokens[r]
                    l += 2
                    r -= 1
                    while leftTotal > rightTotal + power and l < r:
                        leftTotal += tokens[l]
                        rightTotal += tokens[r]
                        l += 1
                        r -= 1
                    if leftTotal <= rightTotal + power:
                        score += 1
                        power += (rightTotal - leftTotal)
                else:
                    break
            
            
        return score