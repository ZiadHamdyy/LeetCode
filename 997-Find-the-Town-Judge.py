class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1

        inD = [0] * (n + 1)
        outD = [0] * (n + 1)

        for a, b in trust:
            outD[a] += 1
            inD[b] += 1

        for person in range(1, n + 1):
            if inD[person] == n - 1 and outD[person] == 0:
                return person

        return -1