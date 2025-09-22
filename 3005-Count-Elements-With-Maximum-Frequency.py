class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_value = max(count.values())

        res = 0
        for k, v in count.items():
            if v == max_value:
                res += v
        return res
