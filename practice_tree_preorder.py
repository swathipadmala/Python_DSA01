class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def preorder(self):
        print(str(self.value)+"---->",end="")

        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

n = Node(5)
n.left = Node(3)
n.right = Node(7)
n.preorder()