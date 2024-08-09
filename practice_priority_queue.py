import heapq
class priorityqueue:
    def __init__(self):
        self.queue = []
    def enqueue(self,item,priority):
        heapq.heappush(self.queue,(priority,item))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def display(self):
        temp = self.queue.copy()
        temp.sort()
        for item,priority in temp:
            print(item,priority)

pq = priorityqueue()
pq.enqueue(10,0)
pq.enqueue(20,3)
pq.enqueue(130,2)
pq.enqueue(140,1)
pq.enqueue(150,4)
pq.dequeue()
pq.display()

