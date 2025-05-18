class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        BIG = 10**9+7

        if m == 1:
            return 3 * pow(2, n-1, BIG) % BIG
        configs = []
        curr = []
        def dfs(r: int) -> None:
            if r == 0:
                for c in 'rgb':
                    curr.append(c)
                    dfs(1)
                    curr.pop()
            elif r == m:
                configs.append(''.join(curr))
            else:
                for c in 'rgb':
                    if c == curr[-1]: continue

                    curr.append(c)
                    dfs(r+1)
                    curr.pop()

        dfs(0)
        C = len(configs)
        T = [[0]*C for _ in range(C)]
        for c1 in range(C):
            for c2 in range(c1):
                if all(a != b for a, b, in zip(configs[c1], configs[c2])):
                    T[c1][c2] = 1
                    T[c2][c1] = 1

        def mult_mod(A, B):
            out = [[0]*C for _ in range(C)]
            for i in range(C):
                for j in range(C):
                    for k in range(C):
                        out[i][j] = (out[i][j] + A[i][k]*B[k][j]) % BIG

            return out
        n -= 1
        Tn = [[0]*C for _ in range(C)]
        for i in range(C): Tn[i][i] = 1
        P = [t[:] for t in T]
        while n:
            if n & 1:
                Tn = mult_mod(Tn, P)
            P = mult_mod(P, P)
            n >>= 1

        return sum(sum(row) for row in Tn) % BIG