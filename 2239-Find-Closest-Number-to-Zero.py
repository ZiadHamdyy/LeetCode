class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        close = 1000000
        for i in nums:
            if abs(i) <= abs(close):
                if close == abs(i):
                    close = abs(i)
                else:
                    close = i
        return close