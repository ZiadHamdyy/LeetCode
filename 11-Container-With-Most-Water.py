class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        l, r = 0, len(height) - 1

        while l <= r:
            if height[l] <= height[r]:
                if maxArea < height[l] * (r - l):
                    maxArea = height[l] * (r - l)
                l += 1
            else:
                if maxArea < height[r] * (r - l):
                    maxArea = height[r] * (r - l)
                r -= 1
        return maxArea