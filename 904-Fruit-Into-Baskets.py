class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = point = total = 0
        for i in range(1, len(fruits)):
            if (fruits[i] != fruits[i - 1] and fruits[i] != fruits[point - 1]):
                left = point
            if (fruits[i] != fruits[i - 1]):
                point = i
            total = max(total, i - left)
        return total + 1
