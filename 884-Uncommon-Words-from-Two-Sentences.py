class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        res = []
        s1 = s1.split()
        s2 = s2.split()
        dic1 = {}
        dic2 = {}
        for w in s1:
            if w not in dic1:
                dic1[w] = 1
            else:
                dic1[w] += 1
        for w in s2:
            if w not in dic2:
                dic2[w] = 1
            else:
                dic2[w] += 1

        for w in s1:
            if w not in dic2 and dic1[w] == 1:
                res.append(w)
        for w in s2:
            if w not in s1 and dic2[w] == 1:
                res.append(w)

        return res