class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        LetterCount = 0
        for i in s:
            if i == letter:
                LetterCount += 1
        return int(LetterCount / len(s) * 100)