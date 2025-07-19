class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        curr = 1
        while curr < len(folder):
            n = len(res[-1])
            if res[-1] + '/' == folder[curr][:n+1]:
                curr += 1
                continue
            res.append(folder[curr])
            curr += 1
        
        return res
