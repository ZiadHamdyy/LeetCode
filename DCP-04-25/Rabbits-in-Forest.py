class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        rabbits = 0
        for key, value in Counter(answers).items():
            group_count = ceil(value / (key + 1))
            rabbits += group_count * (key + 1)
        return rabbits