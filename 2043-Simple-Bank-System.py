class Bank:
    def __init__(self, balance: List[int]):
        self.dic = {}
        self.n = len(balance)
        for i in range(self.n):
            self.dic[i+1] = balance[i]
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 < 1 or account1 > self.n or account2 < 1 or account2 > self.n:
            return False
        if self.dic[account1] >= money:
            self.dic[account1] -= money
            self.dic[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        self.dic[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account < 1 or account > self.n:
            return False
        if self.dic[account] >= money:
            self.dic[account] -= money
            return True
        return False
