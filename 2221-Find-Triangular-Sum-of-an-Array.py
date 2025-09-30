class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            next_arr = []
            for i in range(len(nums) - 1):
                next_arr.append((nums[i] + nums[i + 1]) % 10)
            nums = next_arr
        return nums[0]
