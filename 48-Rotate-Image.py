class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        \\\
        Do not return anything, modify matrix in-place instead.
        \\\
        row = []
        n = len(matrix)
        for i in matrix:
            for j in i:
                row.append(j)
        
        for i in range(len(matrix)):
            n = len(matrix) - i
            for j in range(len(matrix[i])):
                matrix[i][j] = row[-n]
                n += len(matrix)