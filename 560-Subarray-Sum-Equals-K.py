class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic = {}
        PSum = 0
        count = 0
        dic[0] = 1
        for i in nums:
            PSum += i
            
            if (PSum - k) in dic:
                count += dic[PSum - k]

            if PSum not in dic:
                dic[PSum] = 1
            else:
                dic[PSum] += 1
        return count