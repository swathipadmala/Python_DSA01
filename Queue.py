class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.insert(0,value)
    def dequeue(self):
        self.queue.pop(0)
    def display(self):
        print(str(self.queue))

s = queue()
s.enqueue(10)
s.enqueue(20)
s.enqueue(20)
s.enqueue(67)
s.enqueue(78)
s.dequeue()
s.display()
