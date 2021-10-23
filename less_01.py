class MyIterator:
    """Пример работы метода range"""
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cursor = None

    def __iter__(self):
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == self.end:
            raise StopIteration
        return self.cursor


my_iterator = MyIterator(1, 10)

for item in my_iterator:
    print(item)
