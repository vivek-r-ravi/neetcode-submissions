class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


# solution 1: singly linked list
# singly linked list is represented by a head
# O(1) for init, addAtHead and deleteAtHead
# O(n) for other functions as linked list is traversed to get to desired node
# O(n) space complexity
# can optimize this by condensing reused code (line 23-26) into another function
class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.head)
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        curr = self.head
        if curr is None:  # if adding new node at tail on empty linked list
            self.head = newNode  # new node becomes the head
        else:
            while curr.next:
                curr = curr.next
            curr.next = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.size:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = Node(val, curr.next)
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.size != 0:
            self.head = self.head.next
            self.size -= 1
        elif index < self.size:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
            self.size -= 1


# solution 2: doubly linked list
# doubly linked list is represented by a head and a tail
# O(1) for init, addAtTail and addAtHead
# O(n) for other functions as linked list is traversed to get to desired node
# addl optimization to determine whether to traverse from head or tail based on index
# O(n) space complexity
# condensed resused code into another function (_get_node)
class MyLinkedListV2:
# class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def _get_node(self, index):
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index - 1):
                curr = curr.prev
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self._get_node(index).val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, None, self.head)
        if self.head is not None:
            self.head.prev = newNode
        else:  # if adding new node at head on empty linked list
            self.tail = newNode  # new node becomes both head and tail
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        newNode = Node(val, self.tail, None)
        if self.tail is not None:
            self.tail.next = newNode
        else:  # if adding new node at head on empty linked list
            self.head = newNode  # new node becomes both head and tail
        self.tail = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index == self.size:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        elif index < self.size:
            curr = self._get_node(index - 1)
            newNode = Node(val, curr, curr.next)
            curr.next.prev = newNode
            curr.next = newNode
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index == 0 and self.size != 0:
            self.head = self.head.next
            if self.size != 1:
                self.head.prev = None
            else:  # if deleting the last node
                self.tail = self.head  # tail and head become None
            self.size -= 1
        elif index == self.size - 1:
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
        elif index < self.size:
            curr = self._get_node(index - 1)
            curr.next.next.prev = curr
            curr.next = curr.next.next
            self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
