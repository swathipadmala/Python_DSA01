class Node:
    def __init__(self,data = None, Next = None):
        self.data = data
        self.Next = Next
class SLL:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end = "")
                temp = temp.Next

s = SLL()
s.insert(10)
s.insert(20)
s.insert(30)
s.insert(40)
s.display()

 