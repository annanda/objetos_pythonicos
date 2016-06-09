from collections import namedtuple
from random import shuffle

Carta = namedtuple('Carta', 'valor naipe')

class Baralho:

    def __init__(self):
        valores = [str(i) for i in range (2, 11)] + 'J Q K A'.split()
        naipes = 'espadas paus copas ouros'.split()

        # faz produto carteziano desses for
        # it does dot product of these for's
        self.cartas = [Carta(valor, naipe)  for naipe in naipes for valor in valores]

    def __repr__(self):
        return repr(self.cartas)

    def __getitem__(self, item):
        return self.cartas[item]

    def __len__(self):
        return len(self.cartas)

    def __setitem__(self, key, value):
        self.cartas[key] = value

b = Baralho()
print(b)
print(b[:5])
shuffle(b)
print(b)