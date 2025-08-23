class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ps = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            r = 0
            for j in range(n):
                r += 1 if grid[i][j] else 0
                ps[i+1][j+1] = ps[i][j+1] + r

        def count_ones(x1, x2, y1, y2):
            if x1 > x2 or y1 > y2: return 0
            return ps[x2+1][y2+1] - ps[x1][y2+1] - ps[x2+1][y1] + ps[x1][y1]

        @lru_cache(None)
        def min1(x1, x2, y1, y2):
            if count_ones(x1, x2, y1, y2) == 0: return float('inf')
            l, r = x1, x2
            while l < r:
                mid = (l + r) // 2
                if count_ones(x1, mid, y1, y2): r = mid
                else: l = mid + 1
            minx = l
            l, r = x1, x2
            while l < r:
                mid = (l + r + 1) // 2
                if count_ones(mid, x2, y1, y2): l = mid
                else: r = mid - 1
            maxx = l
            l, r = y1, y2
            while l < r:
                mid = (l + r) // 2
                if count_ones(x1, x2, y1, mid): r = mid
                else: l = mid + 1
            miny = l
            l, r = y1, y2
            while l < r:
                mid = (l + r + 1) // 2
                if count_ones(x1, x2, mid, y2): l = mid
                else: r = mid - 1
            maxy = l
            return (maxx - minx + 1) * (maxy - miny + 1)

        @lru_cache(None)
        def min2(x1, x2, y1, y2):
            ans = math.inf
            for k in range(x1, x2):
                ans = min(ans, min1(x1, k, y1, y2) + min1(k+1, x2, y1, y2))
            for k in range(y1, y2):
                ans = min(ans, min1(x1, x2, y1, k) + min1(x1, x2, k+1, y2))
            return ans

        res = math.inf
        for i in range(m-1):
            res = min(res,
                      min2(0, i, 0, n-1) + min1(i+1, m-1, 0, n-1),
                      min2(i+1, m-1, 0, n-1) + min1(0, i, 0, n-1))
        for j in range(n-1):
            res = min(res,
                      min2(0, m-1, 0, j) + min1(0, m-1, j+1, n-1),
                      min2(0, m-1, j+1, n-1) + min1(0, m-1, 0, j))
        return res
