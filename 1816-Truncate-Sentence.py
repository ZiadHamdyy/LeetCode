class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        result = []
        for i in range(k):
            result.append(arr[i])
        return " ".join(result)