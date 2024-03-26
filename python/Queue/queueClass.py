from collections import deque



class Queue:

    def __init__(self):
        self.queue = deque()

    def enqueue(self,val):
        return self.queue.a

    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        return self.queue[0]
    def is_Empty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)
    


q = Queue()

q.enqueue(142)
q.enqueue(150)
q.enqueue(162)
q.enqueue(182)
q.enqueue(190)

q.dequeue()
q.dequeue()
queueValue = q.peek()
print(queueValue) 