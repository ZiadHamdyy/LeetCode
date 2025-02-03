class Solution:
    def trap(self, height: List[int]) -> int:
        trapping = 0
        stack = []
        for i, v in enumerate(height):
            while stack and stack[-1][0] < v:
                lastValue = stack.pop()
                if not stack:
                    break
                leftValue = stack[-1]
                distance = i - leftValue[1] - 1
                height_diff = min(leftValue[0], v) - lastValue[0]
                trapping += distance * height_diff
            stack.append([v, i])
        return trapping