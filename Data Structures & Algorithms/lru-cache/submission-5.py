# brute force
# O(n) time for get and put
# O(n) space
class LRUCacheV1:
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                tmp[1] = value
                self.cache.append(tmp)
                return
        if self.capacity == len(self.cache):
            self.cache.pop(0)
        self.cache.append([key, value])


# canonical solution: hash map + doubly linked list
# using dummy nodes simplifies edge cases and makes code cleaner
# O(1) time for get and put
# O(n) space
class Node:
    def __init__(self, key: int, val: int, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:  # using dummy nodes
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._delete(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.next.key)
            self._delete(self.head.next)

    def _delete(self, curr: Node) -> None:
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def _insert(self, curr: Node) -> None:
        self.tail.prev.next = curr
        curr.prev = self.tail.prev
        curr.next = self.tail
        self.tail.prev = curr


class LRUCacheV3:  # without using dummy nodes
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._delete(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.capacity:
            self.cache.pop(self.head.key)
            self._delete(self.head)

    def _delete(self, curr: Node) -> None:
        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        if curr == self.head:
            curr.next.prev = curr.prev
            self.head = self.head.next
            return
        if curr == self.tail:
            curr.prev.next = curr.next
            self.tail = self.tail.prev
            return
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

    def _insert(self, curr: Node) -> None:
        if not self.tail:
            self.tail = curr
            self.head = curr
            return
        self.tail.next = curr
        curr.prev = self.tail
        curr.next = None
        self.tail = curr


# another canonical solution: hash map only
# O(1) time for get and put
# O(n) space
class LRUCacheV4:
    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache[key] = self.cache.pop(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.pop(next(iter(self.cache)))
