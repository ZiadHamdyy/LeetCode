class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                n = max(n, int(num[i]))
        if n >= 0:
            return str(n) * 3
        return ""
