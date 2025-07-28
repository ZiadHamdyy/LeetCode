class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = Counter([0])
        max_or = 0
        for num in nums:
            for val, count in list(dp.items()):
                dp[val | num] += count
            max_or |= num

        return dp[max_or]
