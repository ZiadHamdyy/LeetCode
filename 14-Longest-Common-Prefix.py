class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for s in strs:
                if i >= len(s) or s[i] != ch:
                    return res
            res += ch
        
        return res
