class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        dp = [[0] * 26 for _ in range(n)]
        queue = deque()

        for i in range(n):
            color_idx = ord(colors[i]) - ord('a')
            dp[i][color_idx] = 1
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        max_color_value = 0

        while queue:
            u = queue.popleft()
            visited += 1
            for v in graph[u]:
                for c in range(26):
                    new_val = dp[u][c] + (1 if c == ord(colors[v]) - ord('a') else 0)
                    if new_val > dp[v][c]:
                        dp[v][c] = new_val
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)
            max_color_value = max(max_color_value, max(dp[u]))

        return -1 if visited < n else max_color_value