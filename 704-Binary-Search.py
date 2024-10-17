class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = int((l + r) / 2)
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
                continue
            elif target < nums[m]:
                r = m - 1
                continue
        return -1

        