class Solution:
    def maximum69Number (self, num: int) -> int:
        c = 0
        a = ''
        num = str(num)
        for i in range(len(num)):
            if num[i] == '6' and c == 0:
                a += '9'
                c = 1
            else:
                a += num[i]
        return int(a)
