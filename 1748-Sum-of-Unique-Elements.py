class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dic = {}
        arr = []
        result = 0

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key, value in dic.items():
            if value == 1:
                arr.append(key)
            else:
                continue

        for i in arr:
            result += i
        return result
