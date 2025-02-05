class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        char_count = {}
        max_freq = 0
        max_length = 0
        while r < len(s):
            char_count[s[r]] = char_count.get(s[r], 0) + 1
            max_freq = max(max_freq, char_count[s[r]])

            if (r - l + 1) - max_freq > k:
                char_count[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length