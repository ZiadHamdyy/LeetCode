class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        l=[words[0]]
        for i in range(1,len(groups)):
            if groups[i]!=groups[i-1]:
                l.append(words[i])
        return l