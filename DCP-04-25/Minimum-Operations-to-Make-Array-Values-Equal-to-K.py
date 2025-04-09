class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        unique = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                unique.add(num)
        return len(unique)