class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        if not meetings:
            return days

        meetings.sort()

        busy_days = 0
        prev_start, prev_end = meetings[0]

        for start, end in meetings[1:]:
            if start <= prev_end + 1:
                prev_end = max(prev_end, end)
            else:
                busy_days += (prev_end - prev_start + 1)
                prev_start, prev_end = start, end

        busy_days += (prev_end - prev_start + 1)

        return days - busy_days
