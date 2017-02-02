"""
Implementando o exemplo do Trem com gerador
"""


class Trem:
    def __init__(self, vagoes):
        self.vagoes = vagoes

    def __iter__(self):
        for i in range(self.vagoes):
            yield 'vagao #{}'.format(i + 1)


