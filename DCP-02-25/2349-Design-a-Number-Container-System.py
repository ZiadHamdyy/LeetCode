class NumberContainers:

    def __init__(self):
       self.index = {}
       self.number = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index:
            oldNum = self.index[index]
        self.index[index] = number
        if number not in self.number:
            self.number[number] = []
        
        heapq.heappush(self.number[number], index)
    def find(self, number: int) -> int:
        if number not in self.number or not self.number[number]:
            return -1
        while self.number[number] and self.index[self.number[number][0]] != number:
            heapq.heappop(self.number[number])
        return self.number[number][0] if self.number[number] else -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)