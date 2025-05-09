class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        n = len(num)
        arr = []
        for e in num:
            arr.append(int(e))
        hs = Counter(arr)
        @cache
        def dfs(node, q, t, sm):

            if node == 10:
                if t == 0 and q ==0:
                    if sm == 0:
                        return 1
                return 0
            ans = 0
            tmp = hs[node]
            for j in range(tmp + 1):
                if j > q or t < tmp - j: continue
                ways = comb(q, j) * comb(t, (tmp - j))
                diff = sm + ((j * node) - ((tmp - j) * node))
                ans += (ways * dfs(node + 1, q - j, t - (tmp - j), diff))
            return ans % (10 ** 9 + 7)
        return (dfs(0, n // 2, n - (n // 2), 0))