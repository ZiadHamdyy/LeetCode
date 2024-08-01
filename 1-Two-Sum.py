class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortnum = sorted(nums)
        index = []
        print(sortnum)
        left = 0
        right = len(sortnum) - 1
        while left < right:
            if sortnum[left] + sortnum[right] == target:
                break
            if sortnum[left] + sortnum[right] < target:
                left = left + 1
            if sortnum[left]+sortnum[right] > target:
                right = right - 1

        print(sortnum[left], sortnum[right])
        for i in range(0, len(nums)):
            if nums[i] == sortnum[left] or nums[i] == sortnum[right]:
                index.append(i)
        return index
        