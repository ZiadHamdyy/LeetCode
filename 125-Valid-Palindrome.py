class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if (
                (i >= \A\ and i <= \Z\)
                or (i >= \a\ and i <= \z\)
                or (i >= \0\ and i <= \9\)
            ):
                arr.append(i)
        toString = \\.join(arr)
        lowercase = toString.lower()
        j = len(lowercase) - 1
        for i in range(len(lowercase) // 2):
            if lowercase[i] != lowercase[j]:
                return False
            if lowercase[i] == lowercase[j]:
                i += 1
                j -= 1
        return True
