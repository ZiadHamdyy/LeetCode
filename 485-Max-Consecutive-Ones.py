class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        r = []
        for i in nums:
            if i == 1:
                count += 1
            else:
                r.append(count)
                count = 0
        r.append(count)
        return sorted(r)[-1]