class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = ['+', '-', '*', '/']
        for i in tokens:
            if i not in op:
                stack.append(int(i))
                continue
        
            num1 = stack.pop()
            num2 = stack.pop()
            if i == '+':
                stack.append(num2 + num1)
            elif i == '-':
                stack.append(num2 - num1)
            elif i == '*':
                stack.append(num2 * num1)
            elif i == '/':
                stack.append(int(num2 / num1))                
        return int(stack[-1])
