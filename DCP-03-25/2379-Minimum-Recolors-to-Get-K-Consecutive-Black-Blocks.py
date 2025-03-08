class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, r = 0, 0
        Wcount = 0
        Min = float('inf')

        while r < len(blocks):
            if blocks[r] == 'W':
                Wcount += 1
            
            if r - l + 1 > k:
                if blocks[l] == 'W':
                    Wcount -= 1
                l += 1
            
            if r - l + 1 == k:
                Min = min(Min, Wcount)
            
            r += 1
        
        return Min

           
