class Stack:
    def __init__(self):
        self.item = []
    def isEmpty(self):
        return self.item == []
    def push(self, s):
        self.item.append(s)
    def pop(self):
        return self.item.pop()
    def peek(self):
        return self.item[len(self) - 1]
    def getsize(self):
        return len(self.item)

s = Stack()
s.push(3)
s.push(5)
print(s.pop())
print(s.pop())