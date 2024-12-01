class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        dic = {}
        arr = list(set(nums1)) + list(set(nums2)) + list(set(nums3))
        result = []
        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for key, value in dic.items():
            if value >= 2:
                result.append(key)
        
        return result
        