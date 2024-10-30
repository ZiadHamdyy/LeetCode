class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strnum = \\
        arr = []
        for i in digits:
            strnum += str(i)
        num = int(strnum) + 1

        for i in str(num):
            arr.append(int(i))
        return arr
