class A:
    def __init__(self,a,b):
        self.__a = a
        self.__b = b
    def showdata(self):
        print('a',self.__a)
        print('b',self.__b)
obj = A(10,20)
obj.showdata()

    
    