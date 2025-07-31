class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        current = set()
        for num in arr:
            new_set = {num}
            for val in current:
                new_set.add(val | num)
            current = new_set
            result.update(current)
        return len(result)
