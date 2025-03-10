class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = "aeiou"
        left = mid = 0
        unique_vowel_count = 0
        frequency = [0] * 6
        temp_frequency = [0] * 6
        total_substrings = 0
        
        for right in range(len(word)):
            vowel_index = vowels.find(word[right]) + 1
            frequency[vowel_index] += 1
            
            if vowel_index > 0 and frequency[vowel_index] == 1:
                unique_vowel_count += 1
            
            while frequency[0] > k:
                left_vowel_index = vowels.find(word[left]) + 1
                frequency[left_vowel_index] -= 1
                
                if left_vowel_index > 0 and frequency[left_vowel_index] == 0:
                    unique_vowel_count -= 1
                left += 1
            
            if unique_vowel_count == 5 and frequency[0] == k:
                if mid < left:
                    mid = left
                    temp_frequency = [0] * 6
                
                while True:
                    mid_vowel_index = vowels.find(word[mid]) + 1

                    if mid_vowel_index == 0 or frequency[mid_vowel_index] - temp_frequency[mid_vowel_index] == 1:
                        break
                    temp_frequency[mid_vowel_index] += 1
                    mid += 1
                
                total_substrings += mid - left + 1
        
        return total_substrings
