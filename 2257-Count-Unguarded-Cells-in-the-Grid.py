class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        unguarded = m * n - len(guards) - len(walls)

        for x, y in guards:
            grid[x][y] = 1
        for x, y in walls:
            grid[x][y] = 2

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for gx, gy in guards:
            for dx, dy in directions:
                x, y = gx + dx, gy + dy
                while 0 <= x < m and 0 <= y < n and grid[x][y] not in (1, 2):
                    if grid[x][y] == 0:
                        grid[x][y] = 3
                        unguarded -= 1
                    x += dx
                    y += dy

        return unguarded
