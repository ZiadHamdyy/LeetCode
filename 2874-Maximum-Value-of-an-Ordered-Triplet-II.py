class Solution:
        def maximumTripletValue(self, nums: List[int]) -> int:
            res = 0
            max_diff = 0
            max_num = 0

            for i in range(len(nums)):
                res = max(res, max_diff * nums[i])
                max_diff = max(max_diff, max_num - nums[i])
                max_num = max(max_num, nums[i])

            return res