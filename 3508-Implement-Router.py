class Router:

    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.q = deque()
        self.seen = set()
        self.dest = defaultdict(list)
        self.proc = defaultdict(int)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.seen: 
            return False
        if len(self.q) == self.memoryLimit: 
            self.forwardPacket()
        self.q.append((source, destination, timestamp))
        self.seen.add((source, destination, timestamp))
        self.dest[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q: 
            return []
        s, d, t = self.q.popleft()
        self.seen.remove((s, d, t))
        self.proc[d] += 1
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        ts = self.dest.get(destination, [])
        lo = self.proc[destination]
        return bisect_right(ts, endTime, lo) - bisect_left(ts, startTime, lo)


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
