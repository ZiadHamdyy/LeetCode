class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = 5000
        while l <= r:
            m = (l + r) // 2
            print(nums[m], res)
            if nums[m] < res:
                res = nums[m]
            if nums[l] >= nums[r] and nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res