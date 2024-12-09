#!/usr/bin/env python3
import random
import math
from ringbuffer import RingBuffer

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        # TO-DO: implement this
        self.capacity =  math.ceil(44100 / frequency)# TO-DO: compute the max capacity of the ring buffer based on the frequency
        self.buffer =  RingBuffer(self.capacity) # TO-DO: construct the ring buffer object
        for i in range(self.capacity):
            self.buffer.enqueue(0.00)
        self.ticks = 0
        self.plucked=set()
        

    @classmethod
    def make_from_array(cls, init: list[int]):
        '''
        Create a guitar string whose size and initial values are given by the array `init`
        '''
        # create GuitarString object with placeholder freq
        stg = cls(1000)

        stg.capacity = len(init)
        stg.buffer = RingBuffer(stg.capacity)
        for x in init:
            stg.buffer.enqueue(x)
        return stg

    def modify_ticks(self, value):
        self.ticks = value
        
    def pluck(self):
        '''
        Set the buffer to white noise
        '''
        # TO-DO: implement this
        size = self.buffer.size()

        for i in range(size):
            self.buffer.dequeue()

        for i in range(size):         
            self.buffer.enqueue(random.uniform(-0.5, 0.5))

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
        # TO-DO: implement this
        ENERGY_DECAY = 0.996

        if self.buffer.size() > 0:
            firstElement = self.buffer.dequeue()
            decay = ENERGY_DECAY*(0.5*(firstElement + self.buffer.peek()))
            self.buffer.enqueue(decay)
            self.ticks += 1

        
    def sample(self) -> float:
        '''
        Return the current sample
        '''
        # TO-DO: implement this
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        # TO-DO: implement this
        return self.ticks
