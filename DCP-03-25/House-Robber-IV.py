class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def can_rob(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        l, r = min(nums), max(nums)
        while l < r:
            mid = (l + r) // 2
            if can_rob(mid):
                r = mid
            else:
                l = mid + 1
        return l