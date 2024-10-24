class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = sorted(nums)
        return arr[0]