#!/usr/bin/env python3
import random
import math
from ringbuffer import RingBuffer

class GuitarString:
    def __init__(self, frequency: float):
        '''
        Create a guitar string of the given frequency, using a sampling rate of 44100 Hz
        '''
        self.capacity =  math.ceil(44100 / frequency)
        self.buffer =  RingBuffer(self.capacity)
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
        size = self.buffer.size()

        for i in range(size):
            self.buffer.dequeue()

        for i in range(size):         
            self.buffer.enqueue(random.uniform(-0.5, 0.5))

    def tick(self):
        '''
        Advance the simulation one time step by applying the Karplus--Strong update
        '''
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
        return self.buffer.peek()

    def time(self) -> int:
        '''
        Return the number of ticks so far
        '''
        return self.ticks
