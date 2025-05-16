class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        dp = [1] * n
        dpp = [-1] * n
        ind = 0
        for i in range(1, n):
            for j in range(i):
                if len(words[i]) == len(words[j]) and sum([1 if c1 != c2 else 0 for c1, c2 in zip(words[i], words[j])]) == 1 and dp[j] > dp[i] - 1 and groups[i] != groups[j]:
                    dp[i] = dp[j] + 1
                    dpp[i] = j
            if dp[i] > dp[ind]:
                ind = i
        output = []
        i = ind
        while i >= 0:
            output.append(words[i])
            i = dpp[i]
        return output[::-1]