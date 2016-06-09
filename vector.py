class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return "Vector({}, {})".format(self.x, self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y
        else:
            raise IndexError("Índice não existe no vetor - Vetor bidimencional")
