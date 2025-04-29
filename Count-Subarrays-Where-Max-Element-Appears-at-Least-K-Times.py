class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        count=0
        mx=max(nums)
        l=0
        mxcnt=0
        for r in range(len(nums)):
            if nums[r]==mx:
                mxcnt+=1
            while mxcnt==k:
                count+=(len(nums)-r)
                if nums[l]==mx:
                    mxcnt-=1
                l+=1
        return count