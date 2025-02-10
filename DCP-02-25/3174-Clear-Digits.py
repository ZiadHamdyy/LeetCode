class Solution:
    def clearDigits(self, s: str) -> str:
        slist = list(s)
        i = 0
        while i < len(slist):
            if slist[i].isdigit():
                slist.pop(i)
                slist.pop(i - 1)
                i -= 2
            i += 1
        return "".join(slist)