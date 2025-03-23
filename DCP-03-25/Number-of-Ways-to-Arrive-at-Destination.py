class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = {i: [] for i in range(n)}

        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        pq = [(0, 0)]
        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        ways = [0] * n
        ways[0] = 1

        while pq:
            time, node = heapq.heappop(pq)

            if time > shortest_time[node]:
                continue

            for neighbor, travel_time in graph[node]:
                new_time = time + travel_time

                if new_time < shortest_time[neighbor]:
                    shortest_time[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (new_time, neighbor))

                elif new_time == shortest_time[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]