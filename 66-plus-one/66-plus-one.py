class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(1, len(digits) + 1):
            if digits[i*(-1)] == 9:
                digits[i*(-1)] = 0
            else:
                digits[i*(-1)] += 1
                break
        
        if digits[0] == 0:
            return [1] + digits
        else:
            return digits
                