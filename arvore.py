class No:
    def __init__(self, valor, esquerdo=None, direito=None):
        self.valor = valor
        self.direito = direito
        self.esquerdo = esquerdo


class Arvore:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def __iter__(self):
        no = self.raiz
        if no:
            yield no.valor
            for filho in Arvore(no.esquerdo):
                yield filho
            for filho in Arvore(no.direito):
                yield filho
            # outra forma de fazer
            # yield from iter(Arvore(no.esquerdo))


neto_direita = No('d')
neto_esquerda = No('c')
filho_esquerdo = No('b', neto_esquerda, neto_direita)
filho_direita = No('e')
no_raiz = No('a', filho_esquerdo, filho_direita)
arvore = Arvore(no_raiz)

for valor in arvore:
    print(valor)