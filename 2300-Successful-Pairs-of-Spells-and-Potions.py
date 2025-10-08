class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        ans = []

        for spell in spells:
            l, r = 0, n - 1
            i = n
            while l <= r:
                m = l + (r - l) // 2
                product = spell * potions[m]
                if product >= success:
                    i = m
                    r = m - 1
                else:
                    l = m + 1
            ans.append(n - i)
        return ans
