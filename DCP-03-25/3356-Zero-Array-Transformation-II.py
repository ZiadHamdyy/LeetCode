class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        total_diff = [0] * (n + 1)
        for l, r, val in queries:
            total_diff[l] += val
            if r + 1 < n:
                total_diff[r + 1] -= val

        sum_total = 0
        for i in range(n):
            sum_total += total_diff[i]
            if sum_total < nums[i]:
                return -1

        low = 0
        high = m
        answer = -1

        while low <= high:
            mid = (low + high) // 2
            diff = [0] * (n + 1)

            for j in range(mid):
                l, r, val = queries[j]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            current_sum = 0
            valid = True
            for i in range(n):
                current_sum += diff[i]
                if current_sum < nums[i]:
                    valid = False
                    break

            if valid:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1

        return answer if answer != -1 else -1
