class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def preorder(self):
        print(str(self.value)+ "---->",end =" ")

        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

root = Node(4)
root.right=Node(45)
root.left=Node(50)
root.preorder()