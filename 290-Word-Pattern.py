class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        ctw = {}
        wtc = {}

        for c, w in zip(pattern, words):
            if c in ctw:
                if ctw[c] != w:
                    return False
            else:
                ctw[c] = w

            if w in wtc:
                if wtc[w] != c:
                    return False
            else:
                wtc[w] = c

        return True