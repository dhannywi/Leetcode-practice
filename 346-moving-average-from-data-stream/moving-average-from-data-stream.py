class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.currSum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.q.append(val)

        if self.count > self.size:
            tail = self.q.popleft()
            self.currSum = self.currSum + val - tail
            return self.currSum / self.size
        else:
            self.currSum += val
            return self.currSum / self.count
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)