from collections import namedtuple

Carta = namedtuple('Carta', 'valor naipe')

class Baralho:

    def __init__(self):
        valores = [str(i) for i in range (2, 11)] + 'J Q K A'.split()
        naipes = 'espadas paus copas ouros'.split()

        # faz produto carteziano desses for
        # it does dot product of these for's
        self.cartas = [Carta(valor, naipe)  for naipe in naipes for valor in valores]

b = Baralho()
print(b.cartas)