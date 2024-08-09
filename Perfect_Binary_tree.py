class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
    
    def insert(self,key):
        if key is None:
            return
        
        if key < self.key:
            if self.left is None:
                self.left = Node(key)
            else:
                self.left.insert(key)

        if key > self.key:
            if self.right is None:
                self.right = Node(key)
            else:
                self.right.insert(key)

    def display(self):
        if self.left:
            self.left.display()

        print('key',self.key)

        if self.right:
            self.right.display()

b = Node(50)
b.insert(30)
b.insert(55)
b.insert(34)
b.insert(38)
b.display()


