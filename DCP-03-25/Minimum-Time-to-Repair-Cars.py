class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time):
            totalRepaired = 0
            for rank in ranks:
                totalRepaired += int((time // rank) ** 0.5)
                if totalRepaired >= cars:
                    return True
            return False

        l, r = 1, min(ranks) * cars * cars
        while l < r:
            mid = (l + r) // 2
            if canRepairInTime(mid):
                r = mid
            else:
                l = mid + 1

        return l