class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums), reverse=True)
        
        if len(unique) >= 3:
            return unique[2]
        else:
            return unique[0]