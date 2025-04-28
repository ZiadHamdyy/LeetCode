class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        sum = 0
        cur_len = 0
        count = 0
        last_idx = 0
        for idx, val in enumerate(nums):
            cur_len += 1
            sum += val
            while sum*cur_len >= k:
                sum -= nums[last_idx]
                cur_len -= 1
                last_idx += 1
            count += idx - last_idx + 1
        
        return count