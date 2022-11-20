class Calculator:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i
    def thing (self):
        for _ in self:
            yield _
max_number = 10
count = Calculator(max_number)
print(count.thing())
print(count.thing().__next__())
for i in count.thing():
    print(i)


