class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        last = float('-inf')
        ans = 0
        for x in nums:
            if x + k > last:
                ans += 1
                last = max(last + 1, x - k)
        return ans
