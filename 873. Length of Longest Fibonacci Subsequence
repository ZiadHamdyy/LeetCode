class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index_map = {v: i for i, v in enumerate(arr)}
        n = len(arr)
        max_len = 0
        dp = [[2] * n for _ in range(n)]
        
        for j in range(n):
            for i in range(j):
                prev = arr[j] - arr[i]
                if prev in index_map and index_map[prev] < i:
                    k = index_map[prev]
                    dp[i][j] = dp[k][i] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
        
        return max_len if max_len >= 3 else 0
