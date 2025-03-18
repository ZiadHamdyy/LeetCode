class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        MaxL = 0
        UsedBit = 0
        l = 0

        for r in range(len(nums)):
            while (UsedBit & nums[r]) != 0:
                UsedBit ^= nums[l]
                l += 1

            UsedBit |= nums[r]
            MaxL = max(MaxL, r - l + 1)

        return MaxL
