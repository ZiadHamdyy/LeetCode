class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        evens = (n + 1) // 2  
        odds = n // 2         
        
        return (pow(5, evens, mod) * pow(4, odds, mod)) % mod