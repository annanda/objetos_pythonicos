"""
Implementando um Trem interável usando o padrão de projeto Iterable
"""

class Trem:

    def __init__(self, vagoes):
        self.vagoes = vagoes

    def __iter__(self):
        return IteradorTrem(self.vagoes)

class IteradorTrem:

    def __init__(self, vagoes):
        self.idx_atual = 0
        self.idx_ultimo_vagao = vagoes - 1

    def __next__(self):
        if self.idx_atual <= self.idx_ultimo_vagao:
            self.idx_atual += 1
            return 'vagão #{}'.format(self.idx_atual)
        else:
            raise StopIteration()

t = Trem(4)
for vagao in t:
    print(vagao)