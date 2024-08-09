class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,value):
        self.queue.insert(0,value)
    def dequeue(self):
        self.queue.pop()
    def get(self,index):
        print(self.queue[index])
    def display(self):
        print(str(self.queue))

q = queue()
q.enqueue(20)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.dequeue()
q.display()
q.get(2)
