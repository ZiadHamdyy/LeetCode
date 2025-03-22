class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        visited = set()
        complete_count = 0

        def dfs(node, component):
            stack = [node]
            visited.add(node)
            while stack:
                curr = stack.pop()
                component.add(curr)
                for neighbor in adj[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)

                num_nodes = len(component)
                num_edges = sum(len(adj[node]) for node in component) // 2
                if num_edges == (num_nodes * (num_nodes - 1)) // 2:
                    complete_count += 1

        return complete_count
