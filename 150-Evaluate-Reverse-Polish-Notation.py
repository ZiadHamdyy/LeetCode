class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if stack and i == '+':
                stack.append(stack.pop() + stack.pop())
            elif stack and i == '-':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 - n1))
            elif stack and i == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2 / n1))
            elif stack and i == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(i))
        return stack[0]