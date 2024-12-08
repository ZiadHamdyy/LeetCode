class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        n = 0
        result = []
        sort = sorted(nums)
        for i in range(len(sort)):
            if sort[i] not in dic:
                dic[sort[i]] = len(nums) - i
        for i in nums:
            result.append(len(nums) - dic[i])
        return result