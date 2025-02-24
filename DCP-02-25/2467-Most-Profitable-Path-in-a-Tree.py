class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        parent = [-1] * n
        depth = [0] * n
        q = deque([0])
        parent[0] = -1
        while q:
            u = q.popleft()
            for v in adj[u]:
                if parent[u] != v and parent[v] == -1:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    q.append(v)
        
        bob_path = []
        current = bob
        while current != -1:
            bob_path.append(current)
            current = parent[current]
        bob_time = {node: i for i, node in enumerate(bob_path)}
        
        leaves = [node for node in range(n) if node != 0 and len(adj[node]) == 1]
        
        max_sum = -float('inf')
        for leaf in leaves:
            current = leaf
            current_sum = 0
            while current != -1:
                if current in bob_time:
                    alice_t = depth[current]
                    bob_t = bob_time[current]
                    if alice_t < bob_t:
                        current_sum += amount[current]
                    elif alice_t == bob_t:
                        current_sum += amount[current] // 2
                else:
                    current_sum += amount[current]
                current = parent[current]
            max_sum = max(max_sum, current_sum)
        
        return max_sum