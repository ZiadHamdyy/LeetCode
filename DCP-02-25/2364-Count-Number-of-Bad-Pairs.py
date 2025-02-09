class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        good = 0

        for i, num in enumerate(nums):
            diff = num - i
            good += freq[diff]
            freq[diff] += 1

        n = len(nums)
        total = (n * (n - 1)) // 2
        return total - good