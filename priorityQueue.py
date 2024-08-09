import heapq

class priorityQueue:
    def __init__(self):
        self.queue = []
    def push(self,item,priority):
        heapq.heappush(self.queue,(priority,item))
    def dequeue(self):
        return heapq.heappop(self.queue)[1]
    def display(self):
        temp = self.queue.copy()
        temp.sort()
        for priority,item in temp:
            print(f"item is:{item},priority:{priority}")

p = priorityQueue()
p.push("item1",2)
p.push("item2",3)
p.push("item3",8)
p.push("item4",15)
p.push("item5",5)
p.display()

