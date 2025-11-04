class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        r = []
        f = {}
        
        for i in range(k):
            f[nums[i]] = f.get(nums[i], 0) + 1
        
        for i in range(n - k + 1):
            s = sorted(f.items(), key=lambda j: (j[1], j[0]), reverse=True)
            r.append(sum(p * q for p, q in s[:x]))
            
            if i + k < n:
                f[nums[i]] -= 1
                if f[nums[i]] == 0:
                    del f[nums[i]]
                f[nums[i + k]] = f.get(nums[i + k], 0) + 1
        
        return r