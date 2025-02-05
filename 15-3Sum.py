class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        res = []
        for i in range(len(nums)):
            dic[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                dic[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if target in dic and dic[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                dic[nums[j]] += 1
        return res