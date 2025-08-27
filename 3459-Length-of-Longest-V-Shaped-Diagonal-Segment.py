class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = {}
        rotation = {
            (1, 1): (1, -1),
            (1, -1): (-1, -1),
            (-1, -1): (-1, 1),
            (-1, 1): (1, 1),
        }

        def search(y, x, dy, dx, turned, need) -> int:
            nonlocal rows, cols
            if y < 0 or x < 0 or y >= rows or x >= cols or grid[y][x] != need:
                return 0
            key = (y, x, dy, dx, turned)
            if key in dp: return dp[key]

            # default search
            score = search(y + dy, x + dx, dy, dx, turned, 2 - need)

            if not turned:
                # can we turn?
                dy, dx = rotation[(dy, dx)]
                score = max(score, search(y + dy, x + dx, dy, dx, True, 2 - need))

            dp[key] = 1 + score
            return dp[key]

        ms = 0
        for y in range(rows):
            for x in range(cols):
                if grid[y][x] != 1: continue
                for dy, dx in rotation.keys():
                    ms = max(ms, 1 + search(y + dy, x + dx, dy, dx, False, 2))

        return ms

