class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        if self.q2:
            self.q1=self.q2+self.q1
            self.q2.popleft()
            self.q2.append(x)
        else:
            self.q2.append(x)

    def pop(self) -> int:
        tmp=self.q2.popleft()
        if len(self.q1)>0:
            self.q2.append(self.q1[0])
            self.q1.popleft()
        return tmp

    def top(self) -> int:
        return self.q2[0]

    def empty(self) -> bool:
        return len(self.q2)==0
        
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()