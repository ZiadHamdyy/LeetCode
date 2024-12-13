class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] == target and nums[r] == target:
                first = l
                last = r
                break
            if nums[l] != target:
                l += 1
            if nums[r] != target:
                r -= 1
        return [first, last]
            