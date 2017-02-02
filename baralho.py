from collections import namedtuple
from random import shuffle

Carta = namedtuple('Carta', 'valor naipe')


class Baralho:
    def __init__(self):
        valores = [str(i) for i in range(2, 11)] + 'J Q K A'.split()
        naipes = 'paus copas espada ouros'.split()
        # é como se fosse um for dentro do outro. O for mais externo é o que vem primeiro
        self.cartas = [Carta(valor, naipe) for naipe in naipes for valor in valores]

    def __repr__(self):
        return repr(self.cartas)

    def __getitem__(self, item):
        return self.cartas[item]

    def __len__(self):
        return len(self.cartas)

    def __setitem__(self, key, value):
        self.cartas[key] = value


baralho = Baralho()
print(baralho)
shuffle(baralho)
mao = baralho[:5]
print(mao)
print(len(baralho))

for carta in baralho:
    print(carta)
