class StockSpanner:

    def __init__(self):
        self.dq1 = deque()      # monotonic (non-decreasing) deque
        self.dq2 = deque()      

    def next(self, price: int) -> int:
        while self.dq1 and self.dq1[-1] >= price:
            self.dq2.append(self.dq1.popleft())
        self.dq1.append(price)
        while self.dq2 and self.dq2[-1] <= self.dq1[-1]:
            self.dq1.appendleft(self.dq2.pop())
        return len(self.dq1)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)