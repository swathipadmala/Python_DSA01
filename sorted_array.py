class sorted:
    def __init__(self):
        self.size = 0
        self.array = []
    def add(self,value):
        i = 0
        while i<len(self.array) and self.array[i]<value:
            i = i+1
        self.array.insert(i,value)
    def get(self,index):
        return self.array[index]
    def print_all(self):
        for i in range(len(self.array)):
            print(self.array[i])

s_array = sorted()
s_array.add(12)
s_array.add(34)
s_array.add(45)
s_array.add(1)
value = s_array.get(3)
print("the value:",value)
s_array.print_all()
