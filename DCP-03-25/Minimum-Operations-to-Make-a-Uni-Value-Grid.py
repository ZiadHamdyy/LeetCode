class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        rem = grid[0][0] % x
        arr = []
        
        for row in grid:
            for num in row:
                if num % x != rem:
                    return -1
                arr.append(num)
        
        arr.sort()
        mid = arr[len(arr) // 2]
        return sum(abs(num - mid) // x for num in arr)
