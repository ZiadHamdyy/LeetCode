class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul = 1
        zero = 0
        arr = []
        for i in nums:
            if i == 0:
                zero += 1
                if zero == 2:
                    return [0] * len(nums)
                continue
            mul *= i
        print(mul)
        for i in range(len(nums)):
            if nums[i] == 0:
                oneZeroArray = [0] * len(nums)
                oneZeroArray[i] = mul
                return oneZeroArray
            res = mul // nums[i]
            arr.append(res)
        print(arr)
        return arr