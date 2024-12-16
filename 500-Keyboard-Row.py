class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        dic = {
            1: set(\qwertyuiop\),
            2: set(\asdfghjkl\),
            3: set(\zxcvbnm\)
        }
        res = []
        for i in words:
            row = 0
            WrongRow = False
            for j in i:
                if row == 0 and j.lower() in dic[1]:
                    row = 1
                elif row == 0 and j.lower() in dic[2]:
                    row = 2
                elif row == 0 and j.lower() in dic[3]:
                    row = 3
                if j.lower() not in dic[row]:
                    WrongRow = True
                    break
            if WrongRow:
                continue
            res.append(i)
        return res
