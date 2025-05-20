class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        que = [0] * (len(nums) + 1)
        cnt = 0
        for l, r in queries:
            que[l] += 1
            que[r + 1] -= 1
        
        for i in range(len(nums)):
            cnt += que[i]
            if cnt < nums[i]:
                return False
        
        return True