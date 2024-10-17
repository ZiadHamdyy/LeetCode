class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        arr = []
        def backtrack(Open, Close):
            if Open == Close == n:
                arr.append(\\.join(stack))
            if Open < n:
                stack.append('(')
                backtrack(Open + 1, Close)
                stack.pop()
            if Close < Open:
                stack.append(')')
                backtrack(Open, Close + 1)
                stack.pop()
        backtrack(0, 0)
        return arr

