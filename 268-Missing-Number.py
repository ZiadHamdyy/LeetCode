class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sort = sorted(nums)
        for i in range(len(sort)):
            if i != sort[i]:
                return i
            continue
        return i + 1