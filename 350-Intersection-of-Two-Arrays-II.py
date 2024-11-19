class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        result = []
        for i in nums2:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1


        for i in nums1:
            if i in dic:
                result.append(i)
                if dic[i] == 1:
                    del dic[i]
                else:
                    dic[i] -= 1
            else:
                continue
        return result

