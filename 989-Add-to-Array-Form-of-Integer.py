class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = 0
        nr = 0
        res = []
        for i in num:
            n *= 10
            n += i
        nr = n + k
        while int(nr) != 0:
            res.append(int(nr % 10))
            nr //= 10
        return res[::-1]
