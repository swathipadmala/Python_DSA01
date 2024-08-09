class Node:
    def __init__(self,data=None,Next = None):
        self.data = data
        self.Next = Next
class single:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node
    
    def display(self):
        n = self.head
        while n is not None:
            print(n.data, "--->",end=" ")
            n = n.Next
        print("None")

    def delete(self,data):
        n = self.head
        prev = None

        while n is not None:
            if n.data == data:

                if prev is None:
                    self.head = n.Next
                else:
                    prev.Next = n.Next
                print(f"the data is {data} delete")
                return
            prev = n
            n = n.Next

        print(f"Node with data {data} not found.")

ll = single()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)
ll.display()

ll.delete(20)
ll.display()

ll.delete(30)
ll.display()

ll.delete(25)
ll.display()