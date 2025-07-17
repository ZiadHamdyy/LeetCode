class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[1] * n for _ in range(k)]

        for i in range(n):
            for j in range(i):
                mod = (nums[i] + nums[j]) % k
                dp[mod][i] = max(dp[mod][i], dp[mod][j] + 1)

        return max(max(arr) for arr in dp)
