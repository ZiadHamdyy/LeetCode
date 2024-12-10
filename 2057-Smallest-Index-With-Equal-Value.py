class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            print(nums[i] % 10, i)
            if i % 10 == nums[i]:
                return i
        return -1