class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        move = [0] * n
        len_int = eventTime - endTime[-1]
        for i in range(n-2, -1, -1):
            if endTime[i] - startTime[i] <= len_int:
                move[i] = 1
            t = startTime[i+1] - endTime[i]
            if t > len_int:
                len_int = t
        len_int = startTime[0]
        for i in range(1, n):
            if endTime[i] - startTime[i] <= len_int:
                move[i] = 1
            t = startTime[i] - endTime[i-1]
            if t > len_int:
                len_int = t
        max_t = 0
        for i in range(n):
            start = 0 if i == 0 else endTime[i-1]
            end = eventTime if i == n - 1 else startTime[i+1]
            t = end - start if move[i] else end - start - endTime[i] + startTime[i]
            if t > max_t:
                max_t = t
        return max_t
