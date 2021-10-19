# Queue is the FIFO (first in first out) data structure
# We can use list to implement queue in python by appending at o position
# The same problem exist in this case also as was encountered in stack (dynamic allocation problem). 


# We can also use deque for the implementation of queue with specification use of operations. 

from collections import deque

class Queue:

    def __init__(self):
        self.container = deque()

    def insert(self, val):             #This will append element from lef side of the queue
        self.container.appendleft(val)

    def fetch(self, val):              #This will fetch element on the FIFO basis 
        return self.container.pop()

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)