class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        dic = set()
        base = 10 ** ((n - 1) // 2)
        skip = n & 1

        for i in range(base, base * 10):
            s = str(i)
            s += s[::-1][skip:]
            pal = int(s)
            if pal % k == 0:
                dic.add("".join(sorted(s)))

        fac = [factorial(i) for i in range(n + 1)]
        ans = 0
        for s in dic:
            count = [0] * 10
            for c in s:
                count[int(c)] += 1
            total = (n - count[0]) * fac[n - 1]
            for x in count:
                total //= fac[x]
            ans += total

        return ans
