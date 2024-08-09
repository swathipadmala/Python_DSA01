class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None

class SLL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("No Data")
        else:
            temp = self.head
            while temp:
                print(temp.data,"----->",end = " ")
                temp  = temp.Next

ll = SLL()
n=Node(10)
ll.head = n
n1 = Node(20)
ll.head.Next = n1
n2 = Node(30)
n1.Next = n2

ll.display()