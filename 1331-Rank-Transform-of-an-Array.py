class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dic = {}
        rank = 1
        rank_results = []
        for i in sorted(arr):
            if i not in dic:
                dic[i] = rank
                rank += 1
            else:
                continue
        for i in arr:
            rank_results.append(dic[i])
        return rank_results