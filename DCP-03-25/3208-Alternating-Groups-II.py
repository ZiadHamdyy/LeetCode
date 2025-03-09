class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k == 1:
            return n
        if k > n:
            return 0
        
        m = k - 1
        
        bad_pairs = [0] * n
        for i in range(n):
            next_i = (i + 1) % n
            if colors[i] == colors[next_i]:
                bad_pairs[i] = 1
        
        extended = bad_pairs * 2
        
        prefix = [0] * (len(extended) + 1)
        for i in range(len(extended)):
            prefix[i + 1] = prefix[i] + extended[i]
        
        count = 0
        for i in range(n):
            end = i + m
            total = prefix[end] - prefix[i]
            if total == 0:
                count += 1
        
        return count
