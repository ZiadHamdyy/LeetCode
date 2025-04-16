class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)

        pairs = 0
        ans = 0
        r = 0
        cnt = Counter()
        for l in range(n):
            while pairs < k and r < n:
                pairs += cnt[nums[r]]
                cnt[nums[r]] += 1
                r += 1
            
            if pairs >= k:
                ans += n - r + 1
            cnt[nums[l]] -= 1
            pairs -= cnt[nums[l]]

        return ans
