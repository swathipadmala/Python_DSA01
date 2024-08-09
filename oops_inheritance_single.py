class A:
    def __init__(self,name,rno):
        self.name = name
        self.rno = rno
    def display(self):
        print("rno",self.rno)
        print("name",self.name)
class B(A):
    def __init__(self,age,rno,name):
     super(). __init__(rno,name)
     self.age = age

    def display(self):
       super().display()
       print("age", self.age)
obj = B(20,"swathi",23)
obj.display()
