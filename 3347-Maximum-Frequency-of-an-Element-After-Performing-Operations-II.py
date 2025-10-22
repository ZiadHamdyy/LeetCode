class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        dict1, ans, max_val = Counter(nums), set(), 1 

        nums.sort()

        for num in nums:
            ans.add(num-k)
            ans.add(num)
            ans.add(num+k)

        for i in ans:
            max_val = max(max_val,dict1[i]+min(bisect.bisect_right(nums,i+k)-bisect.bisect_left(nums,i-k)-dict1[i],numOperations))

        return max_val 
