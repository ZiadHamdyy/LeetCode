class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        @lru_cache(None)
        def dp(left, right, curPlayers, numGamesAlreadyPlayed):
            if left > right:  
                dp(right, left, curPlayers, numGamesAlreadyPlayed)
            if left == right: 
                ans.add(numGamesAlreadyPlayed)
            for i in range(1, left + 1):
                for j in range(left - i + 1, right - i + 1):
                    if not (curPlayers + 1) // 2 >= i + j >= left + right - curPlayers // 2: 
                        continue
                    dp(i, j, (curPlayers + 1) // 2, numGamesAlreadyPlayed + 1)

        ans = set()
        dp(firstPlayer, n - secondPlayer + 1, n, 1)
        return [min(ans), max(ans)]
