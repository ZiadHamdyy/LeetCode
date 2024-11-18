class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s2 = set(nums2)
        lenght = 0
        result = []

        for i in nums1:
            if i in s2 and i not in result:
                result.append(i)
            else:
                continue
        return result