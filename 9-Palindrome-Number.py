class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr = list(str(x))
        l, r = 0, len(arr) - 1

        while l <= r:
            if arr[l] != arr[r]:
                return False
            else:
                l += 1
                r -= 1
        return True