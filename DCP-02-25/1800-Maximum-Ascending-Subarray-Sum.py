class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        MSum = 0
        curSum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curSum += nums[i]
            else:
                MSum = max(MSum, curSum)
                curSum = nums[i]
        
        return max(MSum, curSum)
