class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        word = list(words[0])
        for i in words[1:]:
            temp = []
            for char in word:
                if char in i:
                    temp.append(char)
                    i = i.replace(char, '', 1)
            word = temp
        return word