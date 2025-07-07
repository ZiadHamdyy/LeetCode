class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        heap = []
        cnt, idx = 0, 0
        maxDay = max(e[1] for e in events)
        for day in range(1, maxDay + 1):
            while idx < len(events) and events[idx][0] <= day:
                heapq.heappush(heap, events[idx][1])
                idx += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                cnt += 1
        return cnt
