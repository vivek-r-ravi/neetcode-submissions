# Doubly Linked List Node
class Node:
    
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head=None
        self.tail=None

    def isEmpty(self) -> bool:
        return self.head is None

    def append(self, value: int) -> None:
        newNode=Node(value,self.tail,None)
        if not self.isEmpty():
            self.tail.next=newNode
        else:                   # if adding new node at head on empty linked list
            self.head=newNode   # new node becomes both head and tail
        self.tail=newNode

    def appendleft(self, value: int) -> None:
        newNode=Node(value,None,self.head)
        if not self.isEmpty():
            self.head.prev=newNode
        else:                   # if adding new node at head on empty linked list
            self.tail=newNode   # new node becomes both head and tail
        self.head=newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        val=self.tail.val
        self.tail=self.tail.prev
        if self.tail:
            self.tail.next=None
        else:                       # if deleting the last node 
            self.head = self.tail   # tail and head become None
        return val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        val=self.head.val
        self.head=self.head.next
        if self.head:
            self.head.prev=None
        else:                       # if deleting the last node 
            self.tail = self.head   # tail and head become None
        return val
