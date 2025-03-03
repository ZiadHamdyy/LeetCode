class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        mid = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num == pivot:
                mid.append(num)
            else:
                right.append(num)
        return left + mid + right
