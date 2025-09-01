class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for p, t in classes:
            delta = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-delta, p, t))
        for _ in range(extraStudents):
            d, p, t = heapq.heappop(h)
            p += 1
            t += 1
            delta = (p+1)/(t+1) - p/t
            heapq.heappush(h, (-delta, p, t))
        return sum(p/t for _, p, t in h) / len(classes)
