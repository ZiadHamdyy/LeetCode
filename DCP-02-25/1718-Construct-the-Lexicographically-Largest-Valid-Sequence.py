class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        def backtrack(index, sequence, used):
            if index == len(sequence):
                return sequence

            if sequence[index] != 0:
                return backtrack(index + 1, sequence, used)

            for num in range(n, 0, -1):
                if num == 1:
                    if not used[num]:
                        sequence[index] = num
                        used[num] = True
                        result = backtrack(index + 1, sequence, used)
                        if result:
                            return result
                        sequence[index] = 0
                        used[num] = False
                else:
                    if not used[num]:
                        if index + num < len(sequence) and sequence[index + num] == 0:
                            sequence[index] = num
                            sequence[index + num] = num
                            used[num] = True
                            result = backtrack(index + 1, sequence, used)
                            if result:
                                return result
                            sequence[index] = 0
                            sequence[index + num] = 0
                            used[num] = False
            return None

        sequence_length = 1 + 2 * (n - 1)
        sequence = [0] * sequence_length
        used = {i: False for i in range(1, n + 1)}

        return backtrack(0, sequence, used)