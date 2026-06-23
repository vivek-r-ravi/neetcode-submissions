# solution 1: use 2 queues
# first queue (q1) contains the stack in reverse order
# second queue (q2) is always empty, but used to append new item to 0 index and swapped with q1
# O(1) on time for all except push (O(n)), O(n) on space
class MyStackV1:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        # q2 is the stack in reverse order, while q1 is empty
        self.q1, self.q2 = self.q2, self.q1  # swap q1 and q2 so that q2 is empty again

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0


# solution 2: use 1 queue
# queue contains the stack in reverse order
# during push, append the new items, loop thru q and remove/re-add existing items
# O(1) on time for all except push (O(n)), O(n) on space
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
