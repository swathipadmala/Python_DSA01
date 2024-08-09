class Node:
    def __init__(self,data=None,Next= None):
        self.data = data
        self.Next = Next
class SLL1:
    def __init__(self):
        self.head = None
    def insert(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node
    def display(self):
        if self.head is None:
            print('No Data')
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,'----->',end = " ")
                temp=temp.Next

ll = SLL1()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(50)
ll.insert(15)
ll.display()
