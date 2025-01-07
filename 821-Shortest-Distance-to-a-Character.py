class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = []
        i = 0

        while i < len(s):
            dis = 0
            l, r = i, i

            while l >= 0 or r < len(s):
                if (l >= 0 and s[l] == c) or (r < len(s) and s[r] == c):
                    answer.append(dis)
                    break
                l -= 1
                r += 1
                dis += 1

            i += 1
        return answer
