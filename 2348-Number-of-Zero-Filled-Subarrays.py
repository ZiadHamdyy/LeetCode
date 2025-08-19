class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        compteur = 0
        streak = 1
        for num in nums :
            if num != 0 :
                streak = 1
            else:
                compteur += streak
                streak += 1
        return (compteur)
