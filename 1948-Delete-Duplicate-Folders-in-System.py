class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        trie = {}

        def insert(s):
            current = trie
            for i in s:
                current = current.setdefault(i, {"#":False})
            
        
        for p in paths:
            insert(p)
        table = {}
        def dfs(root):
            if  len(root) == 1 and "#" in root:
                return [""]
            ans = []
            for k in root:
                if k == "#":
                    continue
                path = dfs(root[k])
                for p in path:
                    ans.append(k+p)

            ans.sort()
            s="-".join(ans)
            if s not in table:
                table[s]=[]
            table[s].append(root)
            return ans


        path = dfs(trie)
        path.sort()
        table.pop("-".join(path))
        for s in table:
            if len(table[s]) > 1:
                for node in table[s]:
                    node["#"] = True
        

        ans = []
        def construct(root, p):
            if "#" in root and root["#"] == True:
                return
            if  len(root) == 1 and "#" in root:
                ans.append(p)
                return
            if p:
                ans.append(p)
            for k in root:
                if k == "#":
                    continue
                construct(root[k], p+[k])
         
            

        construct(trie, [])
        return ans
