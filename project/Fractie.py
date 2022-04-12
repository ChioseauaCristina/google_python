class Fractie:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'{self.numarator} / {self.numitor}'

    def __add__(self):
        return self.numarator + self.numitor

    def __sub__(self):
        return self.numarator - self.numitor

    def inverse(self):
        return Fractie(self.numitor, self.numarator)


fractie = Fractie(6, 2)
print(fractie)
inverse = fractie.inverse()
print(inverse)
print(fractie.__add__())
print(fractie.__sub__())
