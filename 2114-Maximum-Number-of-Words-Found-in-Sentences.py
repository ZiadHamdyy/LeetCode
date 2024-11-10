class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        dic = {}
        for i in sentences:
            sentNum = len(i.split(" "))
            dic[i] = sentNum
        print(dic)

        maxsentNum = 0
        for k, v in dic.items():
            if maxsentNum < v:
                maxsentNum = v
            else:
                continue
        return maxsentNum