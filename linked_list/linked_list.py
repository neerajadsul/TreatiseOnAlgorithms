class Node:
    __slots__ = '_value', '_next'
    def __init__(self, value, next):
        self._value = value
        self._next = next


class StackLinkedList:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def push(self, value):
        self._head = Node(value=value, next=self._head)
        self._size += 1
        
    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self._head._value
        
    def pop(self):
        result = self.top()
        self._head = self._head._next
        self._size -= 1
        return result
        

class QueueLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
        
    def is_empty(self):
        return self._size == 0
        
    def first(self):
        if self.is_empty():
            raise Exception('Queue is empty.')
        return self._head._value
        
    def enqueue(self, value):
        new_node = Node(value=value, next=None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1
        
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty.')
        result = self._head._value
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return result
