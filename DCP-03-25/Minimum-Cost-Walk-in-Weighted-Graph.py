class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [i for i in range(n)]
        min_and = [(1 << 20) - 1 for _ in range(n)]

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v, w):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_v] = root_u
                min_and[root_u] &= min_and[root_v] & w
            else:
                min_and[root_u] &= w

        for u, v, w in edges:
            union(u, v, w)

        result = []
        for s, t in query:
            if s == t:
                result.append(0)
                continue
            root_s = find(s)
            root_t = find(t)
            if root_s != root_t:
                result.append(-1)
            else:
                result.append(min_and[root_s])
        return result