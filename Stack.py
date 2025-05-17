from encodings.punycode import selective_find


class Stack:
    def __init__(self):
        self.arr = []
        self.size = 10

    def is_not_empty(self):
        return len(self.arr) > 0

    def pop(self):
        if self.is_not_empty():
            self.arr.pop()

    def has_space(self):
        return len(self.arr) < self.size

    def push(self, value):
        if self.has_space():
            self.arr.append(value)

    def top(self):
        if self.is_not_empty():
            return self.arr[-1]


instance = Stack()
instance.push(1)
instance.push(2)
instance.push(3)
instance.push(4)
instance.push(5)
instance.push(6)
instance.push(7)
print(instance.arr)
instance.pop()
print(instance.arr)