class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums[0])
        ones_string = "1" * n
        max_value = int(ones_string, 2)
        for i in range(max_value):
            Bin = format(i, f'0{n}b')
            if Bin not in s:
                return Bin
        return ones_string
