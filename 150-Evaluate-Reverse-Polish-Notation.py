class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            result = 0
            if i == \+\:
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif i == \-\:
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 - num1
                stack.append(int(result))
            elif i == \*\:
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif i == \/\:
                num1 = stack.pop()
                num2 = stack.pop()
                result = num2 / num1
                stack.append(int(result))
            else:
                stack.append(int(i))

        return stack[0]