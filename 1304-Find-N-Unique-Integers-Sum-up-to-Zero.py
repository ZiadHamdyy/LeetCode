class Solution:
    def sumZero(self, n: int) -> List[int]:
        return ([0] if n % 2 else []) + [x for i in range(1, n // 2 + 1) for x in (i, -i)]

