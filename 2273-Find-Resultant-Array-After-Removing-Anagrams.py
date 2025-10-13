class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        for i in words:
            if res and sorted(res[-1]) == sorted(i):
                continue
            res.append(i)
        return res
