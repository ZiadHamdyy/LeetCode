class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dic = {}
        res = []
        for i in nums1:
            if i[0] not in dic:
                dic[i[0]] = i[1]
            else:
                dic[i[0]] += i[1]
        for i in nums2:
            if i[0] not in dic:
                dic[i[0]] = i[1]
            else:
                dic[i[0]] += i[1]
        for Id, Val in sorted(dic.items()):
            res.append([Id, Val])
        return res

