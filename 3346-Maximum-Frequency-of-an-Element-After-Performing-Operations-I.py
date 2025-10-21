class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        M = max(nums)
        dp = [0] * (M + 1)
        prev = ans = 0
        for i in nums:
            dp[i] += 1
        curr = sum(dp[:k])

        for i in range(M + 1):
            curr -= dp[i]
            if i + k <= M:
                curr += dp[i + k]
            if i > 0:
                prev += dp[i - 1]
            if i > k + 1:
                prev -= dp[i - k - 1]
            ans = max(ans, dp[i] + min(numOperations, prev + curr))
        return ans
