class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        p = sorted(counter.keys())
        n = len(p)
        res = 0
        dp = [0] * (n + 1)
        for i in range(n):
            j = i-1
            while j >= 0 and p[j] >= p[i]-2:
                j -= 1
            dp[i+1] = max(dp[i],dp[j+1] + p[i]*counter[p[i]])
        return dp[-1]
