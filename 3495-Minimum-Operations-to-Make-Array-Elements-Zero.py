class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def ops(query):
            res0, x = 0, 1
            while x < query[0]:
                res0 += 1
                x *= 4
            res1, res, prev = res0, 0, query[0]
            while x <= query[1] * 4:
                res += res1 * (min(x, query[1] + 1) - prev)
                prev, res1, x = x, res1 + 1, x * 4
            return (res + 1) // 2

        return sum(ops(q) for q in queries)
