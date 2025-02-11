class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        partL = list(part)
        for i in range(len(s)):
            stack.append(s[i])
            if stack and stack[-n:] == partL:
                for _ in range(n):
                    stack.pop()
        return "".join(stack)