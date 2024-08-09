class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(str(self.value)+ "---->",end = " ")

        if self.right:
            self.right.inorder()
root = Node(5)
root.left = Node(10)
root.right = Node(30)
root.inorder()
