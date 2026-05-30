class Node:

    def __init__(self, val, prev=None, next=None):
        self.val=val
        self.prev=prev
        self.next=next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr=Node(homepage)

    def visit(self, url: str) -> None:
        self.curr.next=Node(url,self.curr)
        self.curr=self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev is not None:
                self.curr=self.curr.prev
            else:
                break
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next is not None:
                self.curr=self.curr.next
            else:
                break
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)