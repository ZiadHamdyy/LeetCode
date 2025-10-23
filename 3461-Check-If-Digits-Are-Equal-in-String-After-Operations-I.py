class Solution:
    def hasSameDigits(self, s: str) -> bool:
        arr = list(s)
        n = len(arr)
        while n > 2:
            for i in range(n - 1):
                digit = (int(arr[i]) + int(arr[i + 1])) % 10
                arr[i] = str(digit)
            n -= 1
        return arr[0] == arr[1]
