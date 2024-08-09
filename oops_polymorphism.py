class Forms:
    def add(self,a,b):
        self.a = a
        self.b = b
        return a+b
obj = Forms()
res = obj.add(10,20)
res1 = obj.add("swathi","padmala")
res2 = obj.add(10,20)
print(res)
print(res1)
print(res2)