# solution 1: singly linked list
# O(1) for init and addAtHeat, O(n) for other functions
# O(n) space complexity
# can optimize this by condensing reused code into another function

class Node:    
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0

    def get(self, index: int) -> int:
        if index>=self.size:
            return -1
        curr=self.head
        for _ in range(index):
            curr=curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val,self.head)
        self.head=newNode
        self.size+=1

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        curr=self.head
        if curr==None:
            self.head=newNode
        else:
            while curr.next:
                curr=curr.next
            curr.next=newNode
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index==self.size:
            self.addAtTail(val)
        elif index==0:
            self.addAtHead(val)
        elif index<self.size:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next
            curr.next=Node(val,curr.next)
            self.size+=1

    def deleteAtIndex(self, index: int) -> None:
        if index==0 and self.size!=0:
            self.head = self.head.next
            self.size-=1
        elif index<self.size:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
            self.size-=1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)