class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sorted_dic = [
            item[0]
            for item in sorted(dic.items(), key=lambda item: item[1], reverse=True)[:k]
        ]
        return sorted_dic
