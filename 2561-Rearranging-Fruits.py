class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        total_count = count1 + count2

        for fruit, total in total_count.items():
            if  total % 2 != 0:
                return -1
        min_cost = min(min(basket1), min(basket2))
        excess1, excess2 = [], []

        for fruit, count in total_count.items():
            half = count // 2
            if count1[fruit] > half:
                excess1.extend([fruit] * (count1[fruit] - half))     
            elif count2[fruit] > half:
                excess2.extend([fruit] * (count2[fruit] - half)) 
        excess1.sort()
        excess2.sort(reverse=True)           


        cost = 0
        for i in range(len(excess1)):
            cost += min(2 * min_cost, excess1[i], excess2[i])

        return cost   


