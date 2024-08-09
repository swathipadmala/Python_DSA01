class A:
    def __init__(self,a,b):
        self._a = a
        self._b = b
class B(A):
    def __init__(self,a,b):
        super() .__init__(a,b)
    def showdata(self):
        print("a",self._a)
        print("b",self._b)
           
obj = B(10,20)
obj.showdata()       