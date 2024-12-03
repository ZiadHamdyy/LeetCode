class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = ""
        for i, char in enumerate(number):
            if char == digit:
                candidate = number[:i] + number[i+1:]
                max_number = max(max_number, candidate)
        return max_number