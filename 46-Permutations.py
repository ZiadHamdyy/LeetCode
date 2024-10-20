class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result , solution = [], []

        def backtrack():
            if len(solution) == len(nums):
                result.append(solution[:])
                return

            for i in nums:
                if i not in solution:
                    solution.append(i)
                    backtrack()
                    solution.pop()
        backtrack()
        return result