class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        s = set(nums)
        for i in s:
            if i - 1 not in s:
                length = 0
                while i + length in s:
                    length += 1
                longest = max(longest, length)
        return longest