class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = int(1e9) + 7
        s = (bin(n)[2:])[::-1]
        arr = []

        for x in range(len(s)):
            if s[x] == "1":
                if not arr:
                    arr.append(2**x)
                else:
                    arr.append((2**x) * arr[-1])
        ans = []
        for q in queries:
            temp_ans = arr[q[1]] // (arr[q[0]-1] if q[0] > 0 else 1)
            ans.append(temp_ans % mod)
        return ans
