class MovingAverage:
    
    def __init__(self, size: int):
        self.size = size
        self.out_list = []
        self.counter = 0

    def next(self, val: int) -> float:
        self.counter += 1
        self.out_list.append(val)
        if self.counter <= self.size and self.counter != 0:
            return sum(self.out_list)/self.counter
        if self.counter > self.size:
            return sum(self.out_list[::-1][:self.size])/self.size


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)