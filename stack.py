class Stack:
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop()
    def display(self):
        print(str(self.stack))

s = Stack()
s.push(10)
s.push(20)
s.push(40)
s.push(80)
s.push(15)
s.pop()
s.pop()
s.display()