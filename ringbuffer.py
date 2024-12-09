#!/usr/bin/env python3

class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''
        # TO-DO: implement this
        self.MAX_CAP = capacity
        self.buffer = [None] * self.MAX_CAP
        self._front = 0
        self._rear = 0
        self.counter = 0

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''
        # TO-DO: implement this
        return self.counter

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''
        # TO-DO: implement this
        return self.size() == 0
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''
        # TO-DO: implement this
        return self.size() == self.MAX_CAP

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''
        # TO-DO: implement this
        if self.is_full():
            raise RingBufferFull()
        
        self.buffer[self._rear] = x
        self._rear = (self._rear + 1) % self.MAX_CAP
        self.counter += 1
        return
    
    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''
        # TO-DO: implement this
        if self.is_empty():
            raise RingBufferEmpty()
          
        item = self.buffer[self._front]
        self.buffer[self._front] = None
        self._front = (self._front+1) % self.MAX_CAP
        self.counter -= 1
        return item

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''
        # TO-DO: implement this
        if(self.is_empty()):
            raise RingBufferEmpty()
        return self.buffer[self._front]


class RingBufferFull(Exception):
    #Raise when RingBuffer is full
    pass

class RingBufferEmpty(Exception):
    #Raise when RingBuffer is empty
    pass
