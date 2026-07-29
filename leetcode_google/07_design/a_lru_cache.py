"""Hash & Linked List
Time complexity: O(1) for both get and put.
Space complexity: O(capacity)
"""
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.h = {} # hash: key -> ptr
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
    
    def _remove(self, node):
        del self.h[node.key]
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _insert(self, node):
        self.h[node.key] = node
        tmp = self.tail.prev
        tmp.next = node
        node.prev = tmp
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.h:
            ptr = self.h[key]
            self._remove(ptr)
            self._insert(ptr)
            return ptr.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            ptr = self.h[key]
            ptr.key = key
            ptr.val = value
            self._remove(ptr)
            self._insert(ptr)
            return
        
        if len(self.h) == self.cap:
            self._remove(self.head.next)
        
        ptr = Node(key, value)
        self._insert(ptr)
        self.h[key] = ptr
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
