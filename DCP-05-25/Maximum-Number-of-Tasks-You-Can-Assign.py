class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        l, r = 0, min(len(tasks), len(workers))

        while l < r:
            m = (l + r + 1) // 2
            usedPills = 0
            avail = workers[-m:]
            canAssign = True

            for t in reversed(tasks[:m]):
                if avail and avail[-1] >= t:
                    avail.pop()
                else:
                    idx = bisect.bisect_left(avail, t - strength)
                    if idx == len(avail) or usedPills == pills:
                        canAssign = False
                        break
                    usedPills += 1
                    avail.pop(idx)

            if canAssign:
                l = m
            else:
                r = m - 1

        return l
