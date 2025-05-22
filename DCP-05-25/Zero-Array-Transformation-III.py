class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        queries.sort(reverse = True)
        available = SortedList()
        current = SortedList()
        for i in range(n):
            while queries and queries[-1][0] == i:
                available.add(queries.pop()[1])
            while current and current[0] < i:
                current.pop(0)
            while len(current) < nums[i]:
                if not available or available[-1] < i: return -1
                current.add(available.pop())
            if len(current) < nums[i]: return -1
        return len(available)