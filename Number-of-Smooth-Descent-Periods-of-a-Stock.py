1class Solution:
2    def getDescentPeriods(self, prices: List[int]) -> int:
3        ans = 0
4        count = 1
5        for i in range(1, len(prices)):
6            if prices[i - 1] - prices[i] == 1:
7                count += 1
8            else:
9                ans += (count * (count + 1)) // 2
10                count = 1
11        ans += (count * (count + 1)) // 2
12        return ans