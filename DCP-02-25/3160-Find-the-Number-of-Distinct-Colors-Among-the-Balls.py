class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        from typing import List
from collections import Counter

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dic = {}
        counter = Counter()
        res = []

        for key, value in queries:
            if key in dic:
                old_value = dic[key]
                counter[old_value] -= 1
                if counter[old_value] == 0:
                    del counter[old_value]

            dic[key] = value
            counter[value] += 1
            
            res.append(len(counter))

        return res
