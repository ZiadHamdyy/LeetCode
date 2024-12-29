class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(\aeiouAEIOU\)
        vowel_list = [char for char in s if char in vowels]
        
        vowel_list.reverse()
        
        result = []
        vowel_index = 0
        
        for char in s:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
        
        return ''.join(result)
        