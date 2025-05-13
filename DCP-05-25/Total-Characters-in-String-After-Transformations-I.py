class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        data = [0] * 26
        for ch in s:
            data[ord(ch) - 97] += 1
        data = deque(data)
        for _ in range(t):
            z = data.pop()
            data.appendleft(z)
            data[1] +=z
        return sum(data) % mod
