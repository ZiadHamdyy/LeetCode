class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for _, v in dic.items():
            if v % 2 != 0:
                return False
        return True