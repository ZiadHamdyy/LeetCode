class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            x = ''.join(sorted(s))
            if x in dic:
                dic[x].append(s)
            else:
                dic[x] = [s]
        arr = []
        for _key, value in dic.items():
            arr.append(value)
        return arr