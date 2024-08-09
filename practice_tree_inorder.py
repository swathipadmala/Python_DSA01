class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def inorder(self):
        if self.left:
            self.left.inorder()

        print(str(self.value)+"---->",end = "")

        if self.right:
            self.right.inorder()

n = Node(3)
n.left = Node(5)
n.right = Node(4)
n.inorder()



