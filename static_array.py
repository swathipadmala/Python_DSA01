class static:
    def __init__(self,size):
        self.size = size
        self.array = [None]*size
    def add(self,index,value):
        if index<0 or index>=self.size:
            raise IndexError("index out of range")
        else :
            self.array[index] = value
    def get(self, index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])

s_array = static(5)
s_array.add(0,22)
s_array.add(1,23)
s_array.add(3,45)
s_array.add(4,56)
s_array.add(2,67)
value = s_array.get(3)
print("selected value:",value)
s_array.print_all()

