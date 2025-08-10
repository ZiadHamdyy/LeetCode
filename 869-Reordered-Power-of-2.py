class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = sorted(str(n))
        length = len(n)
        for i in range(100):
            num = str(2 ** i)
            if len(num) < length:
                continue
            if len(num) > length:
                return False
            if sorted(num) == n:
                return True
