class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i % 2 == 0:
                if i not in dic:
                    dic[i] = 1
                else:
                    dic[i] += 1
        print(dic)
        if not dic:
            return -1
        most_frequent = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
        
        return most_frequent[0][0]