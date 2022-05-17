class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for val in tokens:
            if val == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 + val2)
            elif val == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                
                stack.append(val2 - val1)
            elif val == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
            elif val == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val1 * val2)
            else:
                stack.append(int(val))
            
        return stack[0]