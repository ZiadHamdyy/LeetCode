class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        res=0
        freq=defaultdict(int)
        for x in words:
            freq[x]+=1
            rev=x[::-1]
            if rev in freq and ((freq[rev]>0 and rev!=x) or (freq[rev]>1 and rev==x)):
                freq[rev]-=1
                freq[x]-=1
                res+=2
        maxi=0
        for i in range(0,26):
            w=chr(i+97)*2
            if freq[w]>0:
                maxi=max(freq[w],maxi)
        res+=maxi
        return res*2
