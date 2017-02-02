class Mamifero:
    pass


class Cao(Mamifero):
    qt_patas = 4
    carnivoro = True
    bravo = False

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

    def __repr__(self):
        return 'Cao(%r)' % self.nome

rex = Cao('Rex')
toto = Cao('Toto')
print(rex)
print(toto)
rex.qt_patas = 6
print(toto.qt_patas)
print(toto.__dict__)
print(rex.__dict__)

