class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.vals = []
        self.count = 0

    def next(self, val: int) -> float:
        self.vals.append(val)
        self.count += 1
        if self.count <= self.size:
            return sum(self.vals) / self.count
        return sum(self.vals[(self.size*-1):]) / self.size
        



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)