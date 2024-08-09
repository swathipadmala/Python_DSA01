class constructor:
    def __init__(self,rno,name):
        self.rno = rno
        self.name = name
    def display(self):
        print("here is constructor class:")
        print("name is " , self.name)
        print("number is ", self.rno)
obj = constructor(4,"swathi")
obj.display()
