class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        total = sum(nums)
        for num in nums:
            curr += num
            if num == 0:
                rem = total - curr
                if rem == curr:
                    res += 2
                if abs(rem - curr) == 1:
                    res += 1
        return res