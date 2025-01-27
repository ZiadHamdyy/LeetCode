class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[r])
            if longest < r - l + 1:
                longest = r - l + 1
        return  longest