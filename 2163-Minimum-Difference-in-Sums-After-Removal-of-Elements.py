class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        third1, third2 = n//3, (n + n)//3

        left, rght = [-num for num in nums[:third1]], nums[third2:]
        smLeft, smRght = [-sum(left)], [sum(rght)]

        heapify(left)
        heapify(rght)
        
        for i in range(third1, third2):
            j = n - i -1
            smLeft.append(smLeft[-1] + heappushpop(left, -nums[i]) + nums[i])
            smRght.append(smRght[-1] - heappushpop(rght,  nums[j]) + nums[j])
            
        return min(map(sub,smLeft, smRght[::-1]))
