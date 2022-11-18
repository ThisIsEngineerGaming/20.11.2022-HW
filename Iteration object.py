class Calculator:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 50
        if self.i > self.max_number:
            raise StopIteration
        return self.i
    def round (number, calculator):
        i = 0
        for _ in range(calculator):
            yield number ** i
            i -= 1
    result = round(2, 8)
    print(result)
    for _ in result:
        print(_)