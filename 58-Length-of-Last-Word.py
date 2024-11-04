class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = re.split(r\[ ,.!?;:'\\]+\, s)
        i = len(arr) - 1
        while i >= 0:
            if arr[i] != \\:
                return len(arr[i])
            i -= 1