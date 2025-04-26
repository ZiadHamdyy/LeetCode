class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count=0
        n=len(nums)
        mn,mx=-1,-1
        left=-1
        for right in range(n):
            if not(minK<=nums[right]<=maxK):
                left=right
            if nums[right]==maxK:
                mx=right
            if nums[right]==minK:
                mn=right
            start=min(mn,mx)
            if start>left:
                count+=start-left
        return count