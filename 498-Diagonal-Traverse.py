class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        answer = []
        for s in range(m + n - 1):
            if s % 2 == 0:
                i = min(s, m - 1)
                j = s - i
                while i >= 0 and j < n:
                    answer.append(mat[i][j])
                    i -= 1
                    j += 1
            else:
                j = min(s, n-1)
                i = s-j
                while j >= 0 and i < m:
                    answer.append(mat[i][j])
                    i += 1
                    j -= 1
        return answer
