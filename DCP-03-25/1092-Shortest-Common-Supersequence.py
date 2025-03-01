class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        i, j = m, n
        lcs = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                lcs.append(str1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        lcs = lcs[::-1]

        res = []
        i = j = k = 0
        while k < len(lcs):
            current_char = lcs[k]
            while i < len(str1) and str1[i] != current_char:
                res.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != current_char:
                res.append(str2[j])
                j += 1
            res.append(current_char)
            i += 1
            j += 1
            k += 1

        res.append(str1[i:])
        res.append(str2[j:])

        return ''.join(res)
