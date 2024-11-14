class Solution:
    def isBalanced(self, num: str) -> bool:
        even = 0
        odd = 0
        for i in range(0, len(num), 2):
            even += int(num[i])
        for i in range(1, len(num), 2):
            odd += int(num[i])
        if even == odd:
            return True
        return False