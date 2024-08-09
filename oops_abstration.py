from abc import ABC

class polygon(ABC):
    def sides(self):
        pass
    def display(self):
        pass
class triangle(polygon):
    def sides(self):
        print("triangle is having three sides")
    def display(self):
        print(" i am trinagle display function")
class rectangular(polygon):
    def sides(self):
        print("rectangular")
    def display(self):
        print("rectangular od display function")

t = triangle()
t.display()
t.sides()
r = rectangular()
r.display()
r.sides()