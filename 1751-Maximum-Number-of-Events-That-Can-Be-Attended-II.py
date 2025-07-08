class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        n = len(events)

        pre = [-1] * n
        for i in range(n):
            low, high = 0, i - 1
            idx = -1
            while low <= high:
                mid = (low + high) // 2
                if events[mid][1] < events[i][0]:
                    idx = mid
                    low = mid + 1
                else:
                    high = mid - 1
            pre[i] = idx

        dp0 = [0] * (n + 1)
        dp1 = [0] * (n + 1)

        for j in range(1, k + 1):
            dp1[0] = 0
            for i in range(1, n + 1):
                take = events[i - 1][2]
                prev_index = pre[i - 1]
                if prev_index != -1:
                    take += dp0[prev_index + 1]
                not_take = dp1[i - 1]
                dp1[i] = max(take, not_take)
            dp0, dp1 = dp1, dp0

        return dp0[n]
