class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def is_happy(s):
            return all(s[i] != s[i + 1] for i in range(len(s) - 1))
        
        happy_strings = sorted(s for s in map("".join, product("abc", repeat=n)) if is_happy(s))

        return happy_strings[k - 1] if k <= len(happy_strings) else ""