class ProductOfNumbers:

    def __init__(self):
        self.dic = {}
        self.maxProd = 1
        self.index = 0
        self.lastZero = -1
    def add(self, num: int) -> None:
        if num == 0:
            self.maxProd = 1
            self.lastZero = self.index
            self.dic[self.index] = 0
        else:
            self.maxProd *= num
            self.dic[self.index] = self.maxProd
        self.index += 1

    def getProduct(self, k: int) -> int:
        start_index = self.index - k
        
        if start_index <= self.lastZero:
            return 0
        
        if start_index == 0:
            return self.maxProd
        
        if start_index - 1 not in self.dic or self.dic[start_index - 1] == 0:
            return self.maxProd
        
        return self.maxProd // self.dic[start_index - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)