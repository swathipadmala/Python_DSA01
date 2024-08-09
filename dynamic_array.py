class dynamic:
    def __init__(self):
        self.size = 0
        self.array = []
    def add(self,value):
        self.array.append(value)
        self.size = self.size+1
    def get(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(self.size):
            print(self.array[i])

d_array = dynamic()
d_array.add(10)
d_array.add(20)
d_array.add(39)
d_array.add(40)
value = d_array.get(2)
print('selected value:',value)
d_array.print_all()