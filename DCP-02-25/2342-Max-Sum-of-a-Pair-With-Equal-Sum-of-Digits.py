class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        dic = {}
        maxSum = -1
        for i in nums:
            n = 0
            num = i
            while num > 0:
                n += num % 10
                num //= 10
            if n in dic:
                dic[n].append(i)
            else:
                dic[n] = [i]
        for v in dic.values():
            if len(v) < 2:
                continue
            v.sort(reverse=True)
            maxSum = max(maxSum, v[0] + v[1])
        return maxSum