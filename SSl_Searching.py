class Node:
    def __init__(self,data=None,Next=None):
        self.data = data
        self.Next = Next

class search:
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        node = Node(data)
        node.Next = self.head
        self.head = node

    def display(self,data):
        n = self.head
        if n is None:
            print("No Data")
        else:
            while n is not None:
                if n.data == data:
                    print("found",n.data)
                    break
                else:
                    print("data not found")
                    break

ll = search()
ll.insert(19)
ll.insert(23)
ll.insert(34)
ll.insert(46)
ll.insert(98)
ll.display(98)
ll.display(89)
