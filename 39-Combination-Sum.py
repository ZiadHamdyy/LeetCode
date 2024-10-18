class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result, solution = [], []
        def backtrack(number: int):
            if number == target:
                s = sorted(solution)
                if s not in result:
                    result.append(s)
                return
            for i in candidates:
                if i + number <= target:
                    solution.append(i)
                    backtrack(number + i)
                    solution.pop()
        backtrack(0)
        return result