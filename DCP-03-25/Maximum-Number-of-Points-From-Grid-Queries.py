class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        row, col = len(grid), len(grid[0])
        res = [0] * len(queries)
        
        heap = [(grid[0][0], 0, 0)]
        directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
        grid[0][0] = 0
        count = 0
        for qi, q in sorted(enumerate(queries), key=lambda x: x[1]):
            while heap and heap[0][0] < q:
                _, i, j = heappop(heap)
                count += 1
                for dx, dy in directions:
                    dr, dc = i + dx, j + dy
                    if dr >= 0 and dr < row and dc >= 0 and dc < col and grid[dr][dc]:
                        heappush(heap, (grid[dr][dc], dr, dc))
                        grid[dr][dc] = 0
            res[qi] = count
        return res