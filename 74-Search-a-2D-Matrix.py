class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = self.getArray(matrix, target)
        print(arr)
        l, r = 0, len(arr) - 1
        while l <= r:
            m = int((l + r) / 2)
            if arr[m] == target:
                return True
            elif target > arr[m]:
                l = m + 1
                continue
            elif target < arr[m]:
                r = m - 1
                continue
        return False

    def getArray(self, matrix: List[List[int]], target: int) -> List[int]:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = int((l + r) / 2)
            if matrix[m][0] <= target and matrix[m][len(matrix[m]) - 1] >= target:
                return matrix[m]
            elif matrix[m][len(matrix[m]) - 1] < target:
                l = m + 1
                continue
            elif matrix[m][0] > target:
                r = m - 1
                continue
        return []
        