class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p, n = 0, 0

        for i in nums:
            if i == 0:
                continue
            if i < 0:
                n += 1
            else:
                p += 1

        return max(p, n)
