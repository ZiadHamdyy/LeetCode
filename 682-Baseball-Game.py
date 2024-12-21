class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        score = 0
        for i in operations:
            if i == \+\:
                arr.append(arr[-1] + arr[-2])
            elif i == \D\:
                arr.append(arr[-1] * 2)
            elif i == \C\:
                arr.pop()
            else:
                arr.append(int(i))
        for i in arr:
            score += i
        return score