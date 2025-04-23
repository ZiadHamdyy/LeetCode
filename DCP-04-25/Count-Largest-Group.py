class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = {}
        for v in range(1,n+1):
            value = 0
            i = v
           
            while i > 0:
                value += (i%10)
                i = i // 10
            if value in groups.keys():
                groups[value] += 1
            else:
                groups[value] = 1
        maxValue = max(groups.values())
        res = sum(1 for v in groups.values() if v == maxValue)        
        return res
