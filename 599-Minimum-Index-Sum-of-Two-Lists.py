class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {}
        d = {}

        for i in range(len(list1)):
            dic[list1[i]] = [i, None]

        for i in range(len(list2)):
            if list2[i] in dic:
                dic[list2[i]][1] = i
            else:
                dic[list2[i]] = [None, i]

        for key, value in dic.items():
            if value[0] is not None and value[1] is not None:
                d[key] = value[0] + value[1]
        
        min_value = min(d.values())

        res = [key for key, value in d.items() if value == min_value]

        return res

        