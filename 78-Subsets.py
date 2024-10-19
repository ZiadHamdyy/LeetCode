class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, solution = [], []

        def backtrack(i: int):
            if i == len(nums):
                return result.append(solution[:])
            
            solution.append(nums[i])
            backtrack(i + 1)

            solution.pop()
            backtrack(i + 1)
        backtrack(0)
        return result