class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        return m * pow(m - 1, n - k - 1, mod) * comb(n - 1, k) % mod
