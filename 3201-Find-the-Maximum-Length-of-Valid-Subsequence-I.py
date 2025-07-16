class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] % 2
        ones = sum(nums)
        zeroes = len(nums) - sum(nums)
        firstNumber = nums[0]
        alternateCount = 1
        for i in range(1, len(nums)):
            if nums[i] != firstNumber:
                firstNumber = nums[i]
                alternateCount += 1
        
        return max(ones, max(zeroes, alternateCount))
