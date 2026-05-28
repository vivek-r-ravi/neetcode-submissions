class Node:    
    
    def __init__(self,val=None,next=None):
        self.val=val
        self.next=next

class LinkedList:
    
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

    def insertHead(self, val: int) -> None:
        newNode=Node(val,self.head)
        self.head=newNode
        self.size+=1

    def insertTail(self, val: int) -> None:
        newNode=Node(val)
        curr=self.head
        if curr==None:
            self.head=newNode
        else:
            while curr.next:
                curr=curr.next
            curr.next=newNode
        self.size+=1

    def remove(self, index: int) -> bool:
        if index==0 and self.size!=0:
            self.head = self.head.next
            self.size-=1
            return True
        elif index<self.size:
            curr=self.head
            for _ in range(index-1):
                curr=curr.next
            curr.next=curr.next.next
            self.size-=1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        curr=self.head
        if curr is None:
            return []
        out=[curr.val]
        while curr.next:
            curr=curr.next
            out.append(curr.val)
        return out
        
