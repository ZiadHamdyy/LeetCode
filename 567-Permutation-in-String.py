class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        sSet = set(s1)
        s1_sorted = sorted(s1)
        l, r = 0, 0

        while r < len(s2):
            if r - l + 1 == len(s1):
                if sorted(s2[l:r+1]) == s1_sorted:
                    return True
                l += 1
            if s2[r] not in sSet:
                r += 1
                l = r
            else:
                r += 1
        
        return False

            