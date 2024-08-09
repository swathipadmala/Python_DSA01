class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None
    def postorder(self):
        if self.left:
            self.left.postorder()

        if self.right:
            self.right.postorder()

        print(str(self.value)+ "----->",end=" ")

root = Node(10)
root.left = Node(3)
root.right = Node(20)
root.postorder()

