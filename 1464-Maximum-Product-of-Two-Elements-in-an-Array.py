class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = sorted(nums)
        return (n[-1] - 1) * (n[-2] - 1)