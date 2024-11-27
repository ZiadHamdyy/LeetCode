class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l, r = 0, len(s) - 1
        arr = list(s)
        while l < r:
            if arr[l].isalpha() and arr[r].isalpha():
                temp = arr[l]
                arr[l] = arr[r]
                arr[r] = temp
                l += 1
                r -= 1
            elif arr[l].isalpha() and not arr[r].isalpha():
                r -= 1
            elif not arr[l].isalpha() and arr[r].isalpha():
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(arr)