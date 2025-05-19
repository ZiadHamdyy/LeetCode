class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if (nums[0]+nums[1]<=nums[2] ) or (nums[1]+nums[2]<=nums[0] ) or (nums[2]+nums[0]<=nums[1]):
            return 'none'

        n = len(set(nums))
        print(n)

        if n == 1:
            return "equilateral"
        elif n == 2:
            return "isosceles"
        else:
            return "scalene"