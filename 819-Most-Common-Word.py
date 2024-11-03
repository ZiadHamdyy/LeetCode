class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr = re.split(r"[ ,.!?;:'""]+", paragraph.lower())
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1.
        banned.append(".")
        banned.append(" ")
        banned.append("")
        for key in banned:
            dic.pop(key, None)
        key = max(dic, key=dic.get)
        return key
