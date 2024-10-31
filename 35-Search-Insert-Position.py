class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r -= 1
            else:
                l += 1
        return m