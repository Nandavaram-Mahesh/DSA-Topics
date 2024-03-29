from collections import deque


class Stack:

    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        return self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]

    def is_Empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    


s = Stack()


s.push(5)
s.push(10)
s.push(15)
s.push(20)


topValue = s.peek()
print(topValue)