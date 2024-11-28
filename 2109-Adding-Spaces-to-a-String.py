class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        arr = []
        space = 0
        for i in range(len(s)):
            if i == spaces[space]:
                if space != len(spaces) - 1:
                    space += 1
                arr.append(" ")
                arr.append(s[i])
            else:
                arr.append(s[i])
        return "".join(arr)