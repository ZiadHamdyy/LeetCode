class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            n = len(s)
            if n % 2 != 0:
                continue
            firstHalf = sum(int(s[j]) for j in range(0, n // 2))
            secondHalf = sum(int(s[j]) for j in range(n // 2, n))
            if firstHalf == secondHalf:
                count += 1
        return count