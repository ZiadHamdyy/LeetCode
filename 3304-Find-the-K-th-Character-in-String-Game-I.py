class Solution:
    def kthCharacter(self, k: int) -> str:
        asc = [0]
        while len(asc) < k:
            length = len(asc)
            for i in range(length):
                asc.append((asc[i] + 1) % 26)
        return chr(asc[k - 1] + ord('a'))
