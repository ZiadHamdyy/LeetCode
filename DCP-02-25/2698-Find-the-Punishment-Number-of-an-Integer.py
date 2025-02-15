class Solution:
    def punishmentNumber(self, n: int) -> int:
        def canPartition(num: int) -> bool:
            square_str = str(num * num)

            def dfs(index: int, current_sum: int) -> bool:
                if index == len(square_str):
                    return current_sum == num

                number = 0
                for i in range(index, len(square_str)):
                    number = number * 10 + int(square_str[i])
                    if dfs(i + 1, current_sum + number):
                        return True
                return False

            return dfs(0, 0)

        total = 0
        for i in range(1, n + 1):
            if canPartition(i):
                total += i * i

        return total