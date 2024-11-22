class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        num = sorted(nums)
        revers = num[::-1]
        return revers[k - 1]