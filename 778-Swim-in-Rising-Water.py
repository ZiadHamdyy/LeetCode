class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        heap = []
        visited = set((0, 0))
        heap.append((grid[0][0], 0, 0))
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            curr, r, c = heapq.heappop(heap)
            if r == n - 1 and c == n - 1:
                return curr
            for dr, dc in dirs:
                nr, nc = dr + r, dc + c
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(curr, grid[nr][nc]), nr, nc))
                    visited.add((nr, nc))
