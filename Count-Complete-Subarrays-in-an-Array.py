class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        res, l = 0, 0
        n, all_arr = len(nums), len(set(nums))
        curr_nums = defaultdict(int)

        for r in range(n):
            curr_nums[nums[r]] += 1
            while len(curr_nums) == all_arr:
                res += n - r
                curr_nums[nums[l]] -= 1

                if curr_nums[nums[l]] == 0:
                    curr_nums.pop(nums[l])
                
                l += 1
        
        return res