class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        cols = len(mat[0])
        res = 0
        heights = [0] * cols
        for row in mat:
            for i in range(cols):
                if row[i] == 1:
                    heights[i] += 1
                else:
                    heights[i] = 0
            stack = []
            dp = [0] * cols
            for j in range(len(heights)):
                while stack and heights[j] <= heights[stack[-1]]:
                    stack.pop()

                if not stack:
                    dp[j] = heights[j] * (j+1)
                else:
                    top = stack[-1]
                    dp[j] = dp[top] + heights[j] * (j- top)
                stack.append(j)
                res += dp[j]
        return res
