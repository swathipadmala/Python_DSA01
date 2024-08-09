class A:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def display(self):
        print("name",self.name)
        print("id",self.id)
class B(A):
    def __init__(self,age,name,id):
        super(). __init__(name,id)
        

    def display(self):
        super().display()
        
class C(B):
    def get(self):
        print("get name",self.name)
obj = C(1,"swathi",45)
obj.get()
obj.display()
