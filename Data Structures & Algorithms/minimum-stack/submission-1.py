class MinStack:
    def __init__(self):
        self.array = []
        # 2nd array that stores minimum value at each level
        self.minStack = []

    def push(self, val: int) -> None:
        self.array.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self) -> None:
        self.array.pop()
        # keep both arrays aligned
        self.minStack.pop()

    def top(self) -> int:
        return self.array[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
