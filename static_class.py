class static:
    def __init__(self,size):
        self.size = size
        self.array = [None]*size
    def add(self,index,value):
        if index < 0 or index >= self.size:
            raise IndexError("Index is not correct")
        else:
            self.array[index] = value
    def get_data(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])

s_array = static(6)
s_array.add(2,22)
s_array.add(1,33)
s_array.add(3,44)
s_array.add(0,55)
s_array.add(4,88)
data=s_array.get_data(4)
print(data)
s_array.print_all()


