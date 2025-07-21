class Solution:
    def makeFancyString(self, s: str) -> str:
        i = 0
        res = []
        while i < len(s):
            if len(res) >= 2 and res[-1] == res[-2] == s[i]:
                i += 1
            else:
                res.append(s[i])
                i += 1
        return "".join(res)
