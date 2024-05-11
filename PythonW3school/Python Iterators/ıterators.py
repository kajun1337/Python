class BenimIterator:
    def __init__(self, maksimum):
        self.maksimum = maksimum
        self.suanki = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.suanki < self.maksimum:
            self.suanki += 1
            return self.suanki
        else:
            raise StopIteration

# Iterator kullanımı
benim_iterator = BenimIterator(5)

# Iterator üzerinden geçme
for eleman in benim_iterator:
    print(eleman)
