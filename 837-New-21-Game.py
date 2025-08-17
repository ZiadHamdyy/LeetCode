class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1
        prev_prob = 1 if 0 < k else 0
        for i in range(1, n + 1):
            dp[i] = prev_prob / maxPts
            if i < k:
                prev_prob += dp[i]
            if 0 <= i - maxPts and i - maxPts < k:
                prev_prob -= dp[i - maxPts]
        return sum(dp[k:])
