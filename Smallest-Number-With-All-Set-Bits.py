class Solution:
    def smallestNumber(self, n: int) -> int:
        binary = ""
        ones = len(bin(n)) - 2
        for i in range(ones):
            binary = binary + '1'
        return int(binary, 2)