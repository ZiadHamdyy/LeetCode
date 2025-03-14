class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
    
        l, r = 1, max(candies)

        while l <= r:
            mid = (l + r) // 2
            piles = sum(pile // mid for pile in candies)

            if piles >= k:
                l = mid + 1
            else:
                r = mid - 1

        return r
