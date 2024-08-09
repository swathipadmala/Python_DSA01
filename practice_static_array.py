class static:
    def __init__(self,size):
        self.size = size
        self.array = size*[None]
    def add(self,index,value):
        if index<0 and index >= self.size:
            raise IndexError("index out of range")
        else:
            self.array[index] = value
    def get(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])

s_array = static(5)
s_array.add(0,20)
s_array.add(1,30)
s_array.add(2,50)
s_array.add(3,40)
s_array.add(4,50)
value = s_array.get(2)
print("the value is:",value)
s_array.print_all()




