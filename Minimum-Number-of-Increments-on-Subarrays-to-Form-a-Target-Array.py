class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        res = prev = 0
        for i in target:
            if i > prev:
                res += i - prev
            prev = i
        return res
