class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = []
        arr = list(str(n))
        counter = 0

        for i in arr[::-1]:
            if counter == 3:
                result.append(".")
                result.append(i)
                counter = 1
            else:
                result.append(i)
                counter += 1

        return "".join(result[::-1])
