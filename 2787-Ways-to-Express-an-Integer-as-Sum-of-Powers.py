class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        exponents = []
        num = 1
        while num**x <= n:
            exponents.append(num ** x)
            num += 1
        dp = [0] * (n + 1)
        dp[0] = 1  
        for exp in exponents:
            for i in range(n, exp - 1, -1):
                dp[i] = (dp[i] + dp[i - exp]) % MOD

        return dp[n]
