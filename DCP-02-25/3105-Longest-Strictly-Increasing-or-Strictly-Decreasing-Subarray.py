class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        increase = 1
        decrease = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increase += 1
                decrease = 1
            elif nums[i] < nums[i - 1]:
                decrease += 1
                increase = 1
            else:
                increase = 1
                decrease = 1

            count = max(count, increase, decrease)

        return count