class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2: return False
        k = s // 2
        dp = [True] + [False] * k
        for x in nums:
            for i in range(k, x - 1, -1): dp[i] |= dp[i - x]
            if dp[k]: return True
        return dp[k]