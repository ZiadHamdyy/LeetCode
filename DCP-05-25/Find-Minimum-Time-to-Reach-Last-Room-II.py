class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        DIRS = [(1,0), (0,1), (-1,0), (0,-1)]
        heap = [(0, 0, 0, 1)]
        moveTime[0][0] = -1

        while heap:
            time, x, y, step_cost = heapq.heappop(heap)

            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m): 
                    continue
                if moveTime[nx][ny] < 0:
                    continue

                unlock_time = moveTime[nx][ny]
                arrival = max(time, unlock_time) + step_cost

                if nx == n-1 and ny == m-1:
                    return arrival

                heapq.heappush(heap, (arrival, nx, ny, 3 - step_cost))
                moveTime[nx][ny] = -1
        return -1