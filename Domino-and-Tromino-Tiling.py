class Solution:
    def numTilings(self, n: int) -> int:
        a = 1
        b = 2
        c = 5

        if n == 1:
            return a
        if n == 2:
            return b
        if n == 3:
            return c

        MOD = 1_000_000_007
        res = 0

        for _ in range(4, n + 1):
            res = (2 * c + a) % MOD

            a, b, c = b, c, res

        return res