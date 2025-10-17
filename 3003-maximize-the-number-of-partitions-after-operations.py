class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        a = [1 << (ord(c) - ord("a")) for c in s]

        @cache
        def dp(i, option, mask):
            if i == len(a):
                return 0
            mask2 = mask | a[i]
            if mask2.bit_count() > k:
                ans = 1 + dp(i + 1, option, a[i])
            else:
                ans = dp(i + 1, option, mask2)

            if option:
                for j in range(26):
                    mask2 = mask | (1 << j)
                    if mask2.bit_count() > k:
                        ans = max(ans, 1 + dp(i + 1, 0, 1 << j))
                    else:
                        ans = max(ans, dp(i + 1, 0, mask2))
            
            return ans

        return dp(0, 1, 0) + 1
