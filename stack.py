# 1.Stack is a data structure in which we put data and retrieval is done as last in first out basis usins push pop operations
# 2.We can use python list as stack but there lies a problem with list.
# 3.List a dynamic data structure, suppose list has a storage of ten elements and when we push eleventh element it relocates to another area
# in storage with larger space leading to the copying of ten elements, this will use lot of resources when we deal with larger data.


# We can implement stack using deque in python 
# Deque supports thread safe memory efficient appends and pops from either side with approximately the same perfomance O(n) on both sides
# You don't have to worry about copying the data in to other area as in list

from collections import deque
stack_struct = deque()

print(dir(stack_struct))    # this will show the operation under deque class


class stack_struct:
    def __init__(self):
        self.container = deque()
      
    # redefining the function of deque class

    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)


