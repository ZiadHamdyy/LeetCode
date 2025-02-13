class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, total = 0, 0, 0
        minlen = float('inf')
        while r < len(nums):
            total += nums[r]
            while total >= target:
                minlen = min(minlen, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        return minlen if minlen != float('inf') else 0