class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = 0
        res = []
        for x in nums:
            total += x
            y = x ^ k
            res.append(y - x)
        res.sort(reverse = True)
        for i in range(0, len(res) - 1, 2):
            if res[i] + res[i + 1] <= 0:
                break
            total += res[i] + res[i + 1 ]
        return total