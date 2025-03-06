class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * 2
        s = set()
        n = len(grid)
        count = 1
        for i in range(n):
            for j in range(n):
                if grid[i][j] in s:
                    ans[0] = grid[i][j]
                s.add(grid[i][j])
        for i in range(n * n):
            if count not in s:
                ans[1] = count
            count += 1
        return ans
